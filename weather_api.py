import requests
from database.db_connection import get_db_connection
from datetime import datetime
from weather_helpers.weather_helpers import WeatherPicture
import json
from config import weather_key


def get_coordinates(city_name):
    """Gets coordinates of chosen city from database"""

    with get_db_connection() as connection:
        with connection.cursor(dictionary=True) as cursor:
            # Temporary code
            cursor.execute(f"""SELECT latitude, longitude FROM cities 
                                WHERE name = '{city_name.title()}'""")
            lat_long = cursor.fetchall()
            return lat_long


# chosen_city = 'London'      # change this to see other city


def get_weather(chosen_city):
    coordinates = get_coordinates(chosen_city)[0]
    lat = coordinates.get('latitude')
    lon = coordinates.get('longitude')

    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={weather_key}&units=metric'
    response = requests.get(url)
    data = response.json()
    weather = data['weather'][0]['description']
    temp = data['main']['temp']
    sunset = datetime.fromtimestamp(data['sys']['sunset'])
    sunrise = datetime.fromtimestamp(data['sys']['sunrise'])
    # name = data['name']           # Sometimes too specific (getting districts of the city)

    get_icon = WeatherPicture(weather)
    icon = get_icon.get_weather_picture()['image_address']

    return {'city': chosen_city.capitalize(), 'weather': weather.capitalize(), 'temp': round(float(temp), 1),
            'sunrise': sunrise, 'sunset': sunset, 'icon': icon}


if __name__ == '__main__':
    print(get_weather('London'))
