from flask import Flask, flash, request, render_template, redirect
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user, login_required

from config import SECRET_KEY
from HolidayHelper.database.users import add_user, email_available, get_user_with_credentials, get_user_by_id
import weather_api
import events_try

app = Flask(__name__)
app.secret_key = SECRET_KEY

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = '/login' # if someone tries to go somewhere they shouldnt we'll just send them to the login form
login_manager.login_message = "Please log in to view this page" #if they try to access page that is forbidden, let's tell them the message
login_manager.login_message_category = 'error'

# #redirect takes users somewhere
# #request above is for extracting info from the form that's associated with the request
# # flash - flashes a message temporarily and is used for password management below
# # render_template allows to glue base and html tabs together
# flask login module allows to save info of a user when they log in as a cookie and allows to then retrieve this info on our app and potentially use that info

class User(UserMixin): #we're doing this to store a user's id as a cookie in order to then return the id

    def __init__(self, user_details):
        self.id = user_details.get('id')  # This one is important - it needs to be called self.id
        self.name = user_details.get('name')
        self.email = user_details.get('email')

# we need to access the info based on user's id by using some functionality from the login manager:
@login_manager.user_loader
def user_loader(user_id):
    user_details = get_user_by_id(user_id) #basically get the user details from the database, get_user_by_id in useres tab,
    if user_details is None:
        return None
    user = User(user_details)
    return user



@app.get('/')
def view_home():
    return render_template("home.html")


@app.get('/login')
def view_login():
    if not current_user.is_anonymous:
        return redirect('/profile')
    return render_template("login.html")


@app.post('/login')
def submit_login():
    if not current_user.is_anonymous:
        return redirect('/profile')
    email = request.form.get('email')
    password = request.form.get('password')
    user = get_user_with_credentials(email, password)
    if user is None:
        flash("Invalid credentials.", 'error')
    else:
        user = User(user) # transform the user into a natural user class and tehn log them in (see class User above)
        login_user(user) #and actually log the user in
        return redirect('/profile')
    return redirect('/login') # if it doesn't work we get redirected to login page again


@app.get('/signup')
def view_signup():
    if not current_user.is_anonymous:
        return redirect('/profile')
    return render_template("signup.html")


@app.post('/signup')
def submit_signup():
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')
    if len(password) < 8:
        flash("Passwords should be at least 8 characters long.", 'error') #flashing message, category error
    elif not email_available(email): # this function is in the users.py tab
        flash("An account with that email already exists.", 'error')
    else:
        add_user(name, email, password)
        flash("New account created.", 'info') #flashing message, category info
        return redirect('/login') # this works with redirect above and redirects the user to login page if the signup successful
    return redirect('/signup') #if it hasn't been redirected to any other page, eg thanks to above else code, if the if or elif code work then it will be redirected to signup page again



@app.post('/logout')
@login_required
def submit_logout():
    logout_user()
    return redirect('login')


@app.get('/profile')
@login_required
def view_profile():
    return render_template("profile.html", user=current_user) #user was an extra variable necessary in the profile.html definition



@app.get('/city/<city>')
@login_required
def view_city(city):
    if city not in ["prague", "london", "barcelona", "budapest"]:
        return redirect("/city/<city>/error")
    else:
        return render_template("city.html", user=current_user, city={'name': city})


@app.get('/city/<city>/error')
@login_required
def view_city_error(city):
    return render_template("city_error.html", user=current_user, city={'name': city})


@app.route('/<city>/weather')
def weather_output(city):
    output = weather_api.get_weather(city)
    return render_template('weather.html', content=output)

@app.route('/<city>/events')
def events_output(city):
    output = events_try.display_events(f'{city}')
    return render_template('events.html', content=output)


if __name__ == '__main__':
    app.run(port=5005)
