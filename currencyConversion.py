import requests
import json

currency_one = input("Choose your current currency: ").upper()


class CurrencyConversion:

    def __init__(self, amount):
        self.amount = amount

    def Hungarian_forint(self):
        # self.currency_one = input("Choose your current currency: ").upper()
        url = f'https://api.frankfurter.app/latest?amount={self.amount}&from={currency_one}&to=HUF'
        response = requests.get(url)
        return 'Ft' + str(response.json()['rates']['HUF'])

    def Euro(self):
        # currency_one = input("Choose your current currency: ").upper()
        url = f'https://api.frankfurter.app/latest?amount={self.amount}&from={currency_one}&to=EUR'
        response = requests.get(url)
        return '€' + str(response.json()['rates']['EUR'])

    def Czech_koruna(self):
        # currency_one = input("Choose your current currency: ").upper()
        url = f'https://api.frankfurter.app/latest?amount={self.amount}&from={currency_one}&to=CZK'
        response = requests.get(url)
        return 'Kč' + str(response.json()['rates']['CZK'])

    def British_Pound(self):
        url = f'https://api.frankfurter.app/latest?amount={self.amount}&from={currency_one}&to=GBP'
        response = requests.get(url)
        return '£' + str(response.json()['rates']['GBP'])


convertor = CurrencyConversion(100)
print(convertor.Czech_koruna())

print(convertor.British_Pound())
