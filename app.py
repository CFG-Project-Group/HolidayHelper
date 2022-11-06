from flask import Flask, flash, request, render_template, redirect
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user, login_required
from config import SECRET_KEY, google_maps_key, weather_key
from database.users import add_user, email_available, get_user_with_credentials, get_user_by_id
from weather_api import GetWeatherInfo
import google_maps
import folium
from events_try import Events
from Google_Translate import translation
from database.db_connection import get_db_connection
from currencyConversion import exchanging


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
        with get_db_connection() as connection:
            with connection.cursor(dictionary=True) as cursor:
                cursor.execute("""INSERT INTO messages
                                         (email, first_name, last_name, message)
                                  VALUES (%s, %s, %s, %s)""", [email, first_name, last_name, message]) # the %s-s allow to avoid sql attacks, normally we would write VALUES ({email}..., but write it this way instead to avoid attacks
                connection.commit()
    return redirect('/contact')


@app.post('/subscribe')
def submit_subscribe():
    email = request.form.get('email')
    if email:
        with get_db_connection() as connection:
            with connection.cursor(dictionary=True) as cursor:
                cursor.execute("""INSERT INTO subscriptions
                                         (email)
                                  VALUES (%s)""", [email]) # the %s-s allow to avoid sql attacks, normally we would write VALUES ({email}..., but write it this way instead to avoid attacks
                connection.commit()
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

def attractions(city):
    output_for_attractions = google_maps.display_attractions(city)
    return output_for_attractions

def maps(city):
    map_center = google_maps.geocode_city(city)
    list_of_places = google_maps.list_of_places(city)
    folium_map = folium.Map(location=map_center, tiles = 'openstreetmap', zoom_start=12)
    for item in list_of_places:
        folium.Marker(location=item[1], popup=item[0]).add_to(folium_map)
    return folium_map._repr_html_()


@app.get('/destinations/<city>')
@login_required
def view_city(city):
    if city not in ["prague", "london", "barcelona", "budapest"]:
        return redirect("/city/<city>/error")
    else:
        return render_template("city.html", user=current_user, city={'name': city},
                               weather=weather_output(city), events=events_output(city), attractions=attractions(city), maps = maps(city)
                               )


@app.get('/destinations/<city>/error')
@login_required
def view_city_error(city):
    return render_template("city_error.html", user=current_user, city={'name': city})


@app.get('/translate')
def view_translate():
    return render_template("translation.html", result={'detectedSourceLanguage': "en"}, title="translate", user=current_user)


@app.post('/translate')
def submit_translate():
    toLan = request.form.get('to')
    text = request.form.get('text')
    output = translation(toLan, text)
    print(output)
    return render_template("translation.html", result=output, user_text=text, toLan=toLan)


@app.route('/destinations/currency', methods=['GET', 'POST'])
def currency_convert():
    converted_currency = ""
    if request.method == 'POST':
        amount = int(request.form["amount"])
        from_currency = request.form["from"]
        to_currency = request.form["to"]
        converted_currency = exchanging(amount, from_currency, to_currency)
    return render_template("currencyconversion.html", title="Translator", user=current_user, converted_output=converted_currency)


def currency_conversion(from_currency, to_currency, amount):
    converted_currency = exchanging(amount, from_currency, to_currency)
    return converted_currency



if __name__ == '__main__':
    app.run()

