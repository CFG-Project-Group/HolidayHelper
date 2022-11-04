import requests
import json
import requests


class CurrencyConversion:

    def __init__(self, amount):
        self.amount = amount

    def Pound_to_Hungarian_forint(self):
        # self.currency_one = input("Choose your current currency: ").upper()
        url = f'https://api.frankfurter.app/latest?amount={self.amount}&from=GBP&to=HUF'
        response = requests.get(url)
        return 'Ft' + ' ' + str(response.json()['rates']['HUF'])

    def Euro_to_Hungarian_forint(self):
        # self.currency_one = input("Choose your current currency: ").upper()
        url = f'https://api.frankfurter.app/latest?amount={self.amount}&from=EUR&to=HUF'
        response = requests.get(url)
        return 'Ft' + ' ' + str(response.json()['rates']['HUF'])
    def Koruna_to_Hungarian_forint(self):
        # self.currency_one = input("Choose your current currency: ").upper()
        url = f'https://api.frankfurter.app/latest?amount={self.amount}&from=CZK&to=HUF'
        response = requests.get(url)
        return 'Ft' + ' ' + str(response.json()['rates']['HUF'])

    def Pound_to_Euro(self):
        # currency_one = input("Choose your current currency: ").upper()
        url = f'https://api.frankfurter.app/latest?amount={self.amount}&from=GBP&to=EUR'
        response = requests.get(url)
        return '€' + str(response.json()['rates']['EUR'])

    def Forint_to_Euro(self):
        # currency_one = input("Choose your current currency: ").upper()
        url = f'https://api.frankfurter.app/latest?amount={self.amount}&from=HUF&to=EUR'
        response = requests.get(url)
        return '€' + str(response.json()['rates']['EUR'])
    def Koruna_to_Euro(self):
        # currency_one = input("Choose your current currency: ").upper()
        url = f'https://api.frankfurter.app/latest?amount={self.amount}&from=CZK&to=EUR'
        response = requests.get(url)
        return '€' + str(response.json()['rates']['EUR'])

    def Pound_to_Czech_koruna(self):
        # currency_one = input("Choose your current currency: ").upper()
        url = f'https://api.frankfurter.app/latest?amount={self.amount}&from=GBP&to=CZK'
        response = requests.get(url)
        return 'Kč' + str(response.json()['rates']['CZK'])
    def Euro_to_Czech_koruna(self):
        # currency_one = input("Choose your current currency: ").upper()
        url = f'https://api.frankfurter.app/latest?amount={self.amount}&from=EUR&to=CZK'
        response = requests.get(url)
        return 'Kč' + str(response.json()['rates']['CZK'])

    def Forint_to_Czech_koruna(self):
        # currency_one = input("Choose your current currency: ").upper()
        url = f'https://api.frankfurter.app/latest?amount={self.amount}&from=HUF&to=CZK'
        response = requests.get(url)
        return 'Kč' + str(response.json()['rates']['CZK'])

    def Forint_to_British_Pound(self):
        url = f'https://api.frankfurter.app/latest?amount={self.amount}&from=HUF&to=GBP'
        response = requests.get(url)
        return '£' + str(response.json()['rates']['GBP'])

    def Euro_to_British_Pound(self):
        url = f'https://api.frankfurter.app/latest?amount={self.amount}&from=EUR&to=GBP'
        response = requests.get(url)
        return '£' + str(response.json()['rates']['GBP'])

    def Koruna_to_British_Pound(self):
        url = f'https://api.frankfurter.app/latest?amount={self.amount}&from=CZK&to=GBP'
        response = requests.get(url)
        return '£' + str(response.json()['rates']['GBP'])

# FORITN TO EURO CHOSEN AS AN EXAMPLE
converter = CurrencyConversion(100)


if __name__ == '__main__':
    print(converter.Forint_to_Euro())