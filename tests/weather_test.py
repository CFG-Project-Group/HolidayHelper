import datetime
from unittest import TestCase, main, mock
from api import weather_api
from api.weather_api import GetWeatherInfo
import json
from weather_helpers.weather_helpers import WeatherPicture
from config import weather_key
import requests


class MyTestGetCoordinates(TestCase):
    def test_get_coordinates_london(self):
        get_info = GetWeatherInfo()
        self.assertEqual(f"{get_info.get_coordinates('London')}",
                         "[{'latitude': Decimal('51.5085'), 'longitude': Decimal('-0.1257')}]")  # add assertion here

    def test_get_coordinates_budapest(self):
        get_info = GetWeatherInfo()
        self.assertEqual(f"{get_info.get_coordinates('Budapest')}",
                         "[{'latitude': Decimal('47.4979'), 'longitude': Decimal('19.0402')}]")

    def test_get_coordinates_barcelona(self):
        get_info = GetWeatherInfo()
        self.assertEqual(f"{get_info.get_coordinates('Barcelona')}",
                         "[{'latitude': Decimal('41.3874'), 'longitude': Decimal('2.1686')}]")

    def test_get_coordinates_prague(self):
        get_info = GetWeatherInfo()
        self.assertEqual(f"{get_info.get_coordinates('Prague')}",
                         "[{'latitude': Decimal('50.0755'), 'longitude': Decimal('14.4378')}]")

    def test_get_coordinates_invalid_city(self):
        get_info = GetWeatherInfo()
        self.assertEqual(f"{get_info.get_coordinates('Paris')}",
                             "[]")


class TestGetWeather(TestCase):
    def test_request_response(self):
        # Send a request to the API server and store the response.
        url = f'https://api.openweathermap.org/data/2.5/weather?lat={51.5085}&lon={-0.1257}&appid={weather_key}&units=metric'
        response = requests.get(url)
        # Confirm that the request-response cycle completed successfully.
        self.assertTrue(response.ok)


    def test_api_keys(self):
        get_weather_info = GetWeatherInfo()
        """Checking if keys hasn't changed - not values as values are not constant"""

        result = get_weather_info.get_weather('London')
        keys_to_compare = ['city', 'weather', 'temp', 'sunrise', 'sunset', 'icon']
        self.assertEqual(list(result.keys()), keys_to_compare)

    def mock_weather_result(self, city):
        with open(f"mock_weather_{city}.json") as file:
            return json.load(file)

    @mock.patch("api.weather_api.requests.get")
    def test_get_weather_barcelona(self, mock_get):
        get_weather_info = GetWeatherInfo()
        expected_response = {'city': 'Barcelona', 'weather': "Few clouds", 'temp': 22.1,
                              'sunrise': datetime.datetime(2022, 11, 1, 6, 22, 30),
                              'sunset': datetime.datetime(2022, 11, 1, 16, 47, 12),
                              'icon': 'https://cdn4.iconfinder.com/data/icons/the-weather-is-nice-today/64/weather_2-512.png'}
        my_mock_response = mock.Mock(status_code=200)
        my_mock_response.json.return_value = self.mock_weather_result('barcelona')
        mock_get.return_value = my_mock_response
        response = get_weather_info.get_weather('barcelona')
        self.assertEqual(response, expected_response)

    @mock.patch("api.weather_api.requests.get")
    def test_get_weather_london(self, mock_get):
        get_weather_info = GetWeatherInfo()
        expected_response = {'city': 'London',
                             'icon': 'https://cdn4.iconfinder.com/data/icons/iconsland-weather/PNG/256x256/Overcast.png',
                             'sunrise': datetime.datetime(2022, 10, 26, 7, 43, 1),
                             'sunset': datetime.datetime(2022, 10, 26, 17, 45, 43),
                             'temp': 14.0,
                             'weather': 'Overcast clouds'}
        my_mock_response = mock.Mock(status_code=200)
        my_mock_response.json.return_value = self.mock_weather_result('london')
        mock_get.return_value = my_mock_response
        response = get_weather_info.get_weather('london')
        self.assertEqual(response, expected_response)


class WeatherHelperTest(TestCase):

    def test_get_picture_address_snow(self):
        weather_helper = WeatherPicture('snow')
        picture_address_from_db = weather_helper.get_picture_address()['image_address']
        address_to_compare = "https://cdn4.iconfinder.com/data/icons/the-weather-is-nice-today/64/weather_35-256.png"
        self.assertEqual(picture_address_from_db, address_to_compare)

    def test_get_picture_address_fog(self):
        weather_helper = WeatherPicture('fog')
        picture_address_from_db = weather_helper.get_picture_address()['image_address']
        address_to_compare = "https://cdn4.iconfinder.com/data/icons/the-weather-is-nice-today/64/weather_30-256.png"
        self.assertEqual(picture_address_from_db, address_to_compare)

    def test_get_picture_address_light_rain(self):
        weather_helper = WeatherPicture('light rain')
        picture_address_from_db = weather_helper.get_picture_address()['image_address']
        address_to_compare = "https://cdn4.iconfinder.com/data/icons/the-weather-is-nice-today/64/weather_7-512.png"
        self.assertEqual(picture_address_from_db, address_to_compare)

    def test_get_picture_address_clear_sky(self):
        weather_helper = WeatherPicture('clear sky')
        picture_address_from_db = weather_helper.get_picture_address()['image_address']
        address_to_compare = "https://cdn4.iconfinder.com/data/icons/the-weather-is-nice-today/64/weather_3-512.png"
        self.assertEqual(picture_address_from_db, address_to_compare)

    def test_get_weather_picture_invalid_input(self):
        weather_helper = WeatherPicture('hello')
        image = weather_helper.get_weather_picture()
        self.assertEqual(image, "https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-weather/draw2.webp")


if __name__ == '__main__':
    main()
