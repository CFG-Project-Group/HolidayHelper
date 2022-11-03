from unittest import TestCase, main, mock
import json
import requests



response_forint = requests.get('https://api.frankfurter.app/latest?amount=100&from=GBP&to=HUF')
response_euro = requests.get('https://api.frankfurter.app/latest?amount=100&from=GBP&to=EUR')
response_koruna = requests.get('https://api.frankfurter.app/latest?amount=100&from=CZK&to=EUR')
response_pound = requests.get('https://api.frankfurter.app/latest?amount=100&from=CZK&to=GBP')


class TestConverterResponse(TestCase):

    def test_hungarian_status_code(self):
        self.assertEqual(response_forint.status_code, 200)

    def test_koruna_to_Euto_request_response(self):
        response = response_koruna
        self.assertTrue(response)

    def test_hungarian_converter_content_type(self):
        self.assertEqual(response_euro.headers['Content-Type'], 'application/json; charset=utf-8')



class TestExchangeRate(TestCase):

    def test_api_keys(self):
        """ As the values in the response differs constantly,
           this test function, tests whether the keys in the response stay the same """
        result = response_koruna.json()
        self.assertEqual(list(result.keys()), ['amount', 'base', 'date', 'rates'])

    def mock_currency_converter(self, currency):
        with open(f"mock_{currency}_exchange.json") as file:
            return json.load(file)

    @mock.patch("currencyConversion.requests.get")
    def test_exchange_to_pound_when_response_is_ok(self, mock_get):
        result = {'amount': 100.0, 'base': 'CZK', 'date': '2022-11-02', 'rates': {'GBP': 3.5134}}
        mock_response = mock.Mock(status_code=200)
        mock_response.json.return_value = self.mock_currency_converter('GBP')
        mock_get.return_value = mock_response
        response = response_pound.json()
        self.assertEqual(response, result)
#

if __name__ == '__main__':
    main()