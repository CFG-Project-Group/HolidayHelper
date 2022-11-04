from flask import Flask, flash, request, render_template, redirect
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user, login_required
from config import SECRET_KEY, google_maps_key
from database.users import add_user, email_available, get_user_with_credentials, get_user_by_id
from weather_api import GetWeatherInfo
import google_maps
from events_try import Events


app = Flask(__name__)
app.secret_key = SECRET_KEY


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = '/'
login_manager.login_message = 'Please log in to view this page'
login_manager.login_message_category = 'error'


class User(UserMixin):

    def __init__(self, user_details):
        self.id = user_details.get('id')
        self.name = user_details.get('name')
        self.email = user_details.get('email')


@login_manager.user_loader
def user_loader(user_id):
    user_details = get_user_by_id(user_id)
    if user_details is None:
        return None
    user = User(user_details)
    return user


@app.get('/')
def view_home():
    return render_template("home.html", title="Home", user=current_user)


@app.get('/destinations')
def view_destinations():
    return render_template("destinations.html", title="Destinations", user=current_user)


@app.get('/about')
def view_about():
    return render_template("about.html", title="About", user=current_user)


@app.get('/contact')
def view_contact():
    return render_template("contact.html", title="Contact", user=current_user)


@app.post('/message')
def submit_message():
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    email = request.form.get('email')
    message = request.form.get('message')
    if first_name and last_name and email and message:
        '''Enter message into database'''
    return redirect('/contact')


@app.post('/subscribe')
def submit_subscribe():
    email = request.form.get('email')
    if email:
        '''Enter email into database'''
    return redirect('/contact')


@app.post('/signin')
def submit_signin():
    if not current_user.is_anonymous:
        return redirect('/')
    email = request.form.get('email')
    password = request.form.get('password')
    user = get_user_with_credentials(email, password)
    if user is None:
        flash("Invalid credentials.", 'error')
    else:
        user = User(user)
        login_user(user)
        return redirect('/profile')
    return redirect('/#signin')


@app.post('/signup')
def submit_signup():
    if not current_user.is_anonymous:
        return redirect('/')
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')
    if len(password) < 8:
        flash("Passwords should be at least 8 characters long.", 'error')
    elif not email_available(email):
        flash("An account with that email already exists.", 'error')
    else:
        add_user(name, email, password)
        flash("New account created.", 'info')
        return redirect('/#signin')
    return redirect('/#signup')


@app.post('/signout')
@login_required
def submit_signout():
    logout_user()
    return redirect('/')


@app.get('/profile')
@login_required
def view_profile():
    return render_template("profile.html", user=current_user)

def weather_output(city):
    get_info = GetWeatherInfo()
    output_weather = get_info.get_weather(city)
    return output_weather

def events_output(city):
    event = Events()
    output_for_events = event.display_events(f'{city}')
    return output_for_events


@app.get('/city/<city>')
@login_required
def view_city(city):
    if city not in ["prague", "london", "barcelona", "budapest"]:
        return redirect("/city/<city>/error")
    else:
        return render_template("city.html", user=current_user, city={'name': city},
                               weather=weather_output(city), events=events_output(city)
                               )


@app.get('/city/<city>/error')
@login_required
def view_city_error(city):
    return render_template("city_error.html", user=current_user, city={'name': city})


if __name__ == '__main__':
    app.run(port=5005)

