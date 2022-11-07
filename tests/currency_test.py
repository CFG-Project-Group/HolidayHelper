from unittest import TestCase, main, mock
import json
import requests
from  currencyConversion import exchanging


response_forint = requests.get('https://api.frankfurter.app/latest?amount=100&from=GBP&to=HUF')
response_euro = requests.get('https://api.frankfurter.app/latest?amount=100&from=GBP&to=EUR')
response_koruna = requests.get('https://api.frankfurter.app/latest?amount=100&from=CZK&to=EUR')
response_pound = requests.get('https://api.frankfurter.app/latest?amount=100&from=CZK&to=GBP')


class TestConverterResponse(TestCase):

    def test_exchanging_status_code(self):
        self.assertEqual(response_forint.status_code, 200)

    def test_exchanging_request_response(self):
        response = response_koruna
        self.assertTrue(response)

    def test_exchanging_content_type(self):
        self.assertEqual(response_euro.headers['Content-Type'], 'application/json; charset=utf-8')


class TestExchangeRate(TestCase):

    def test_api_keys(self):
        """ As the values in the response differs constantly,
           this test function, tests whether the keys in the response stay the same """
        result = response_koruna.json()
        self.assertEqual(list(result.keys()), ['amount', 'base', 'date', 'rates'])

    def mock_exchanging(self, currency):
        with open(f"mock_GBP_exchange.json") as file:
            return json.load(file)

    @mock.patch("currencyConversion.requests.get")
    def test_exchanging_when_response_is_ok(self, mock_get):
        result = {'amount': 100.0, 'base': 'CZK', 'date': '2022-11-04', 'rates': {'GBP': 3.582}}
        mock_response = mock.Mock(status_code=200)
        mock_response.json.return_value = self.mock_exchanging('GBP')
        mock_get.return_value = mock_response
        response = exchanging(100, 'CZK', 'GBP')
        self.assertEqual(response, result['rates']['GBP'])


if __name__ == '__main__':
    main()