import requests
import json
import requests


def exchanging(amount, from_currency, to_currency):
    if from_currency == to_currency:
        return "Your request is not valid! Please try another currency. "
    else:
        url = f'https://api.frankfurter.app/latest?amount={amount}&from={from_currency}&to={to_currency}'
        response = requests.get(url)
        return response.json()['rates'][to_currency]


# Example
if __name__ == '__main__':
    print(exchanging(100, "HUF", "HUF"))