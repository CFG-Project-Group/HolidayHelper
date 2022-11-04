import os
from google.cloud import translate_v2
import requests

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'GoogleKey.json'

text = input("input: ")

class Translator:

    def __init__(self, text):
        self.translate_client = translate_v2.Client()
        self.text = text

    def czech_translator(self):
        target = "cs"
        output = self.translate_client.translate(self.text, target_language=target)
        return output['translatedText'].lower()

    def spanish_translator(self):
        target = "es"
        output = self.translate_client.translate(self.text, target_language=target)
        return output['translatedText'].lower()

    def hungarian_translator(self):
        target = "hu"
        output = self.translate_client.translate(self.text, target_language=target)
        return output['translatedText'].lower()


translator = Translator(text)

#choosing spanish as an example

if __name__ == '__main__':
    print(translator.spanish_translator())
