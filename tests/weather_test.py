import datetime
from unittest import TestCase, main, mock
from io import StringIO
from weather_api import get_coordinates, get_weather
import json


class MyTestGetCoordinates(TestCase):
    def test_get_coordinates_london(self):
        self.assertEqual(f"{get_coordinates('London')}",
                         "[{'latitude': Decimal('51.5085'), 'longitude': Decimal('-0.1257')}]")  # add assertion here

    def test_get_coordinates_budapest(self):
        self.assertEqual(f"{get_coordinates('Budapest')}",
                         "[{'latitude': Decimal('47.4979'), 'longitude': Decimal('19.0402')}]")

    def test_get_coordinates_barcelona(self):
        self.assertEqual(f"{get_coordinates('Barcelona')}",
                         "[{'latitude': Decimal('41.3874'), 'longitude': Decimal('2.1686')}]")

    def test_get_coordinates_prague(self):
        self.assertEqual(f"{get_coordinates('Prague')}",
                         "[{'latitude': Decimal('50.0755'), 'longitude': Decimal('14.4378')}]")

    def test_get_coordinates_invalid_city(self):
        self.assertEqual(f"{get_coordinates('Paris')}",
                             "[]")


class TestGetWeather(TestCase):
    def mock_weather_result(self, city):
        with open(f"mock_weather_{city}.json") as file:
            return json.load(file)

    @mock.patch("weather_api.requests.get")
    def test_get_weather_barcelona(self, mock_get):

        """Check if keys are the same - not values"""

        fake_response = {'city': 'Barcelona', 'weather': "Few clouds", 'temp': 21.2,
                              'sunrise': datetime.datetime(2022, 10, 26, 7, 15, 19),
                              'sunset': datetime.datetime(2022, 10, 26, 17, 55, 2)}
        my_mock_response = mock.Mock(status_code=200)
        my_mock_response.json.return_value = self.mock_weather_result('barcelona')
        mock_get.return_value = my_mock_response
        response = get_weather(city='barcelona')
        self.assertEqual(response, fake_response)


if __name__ == '__main__':
    main()
