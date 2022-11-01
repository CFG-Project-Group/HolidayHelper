import os
from google.cloud import translate_v2
from API_config import APIkeys


API_key = APIkeys()
key = API_key.get_translator_key()
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = key


class Translator:

    def __init__(self):
        self.translate_client = translate_v2.Client()

    def czech_translator(self, text):
        target = "cs"
        output = self.translate_client.translate(text, target_language=target)
        return output['translatedText'].lower()

    def spanish_translator(self, text):
        target = "es"
        output = self.translate_client.translate(text, target_language=target)
        return output['translatedText'].lower()

    def hungarian_translator(self, text):
        target = "hu"
        output = self.translate_client.translate(text, target_language=target)
        return output['translatedText'].lower()


# #
# translator = Translator()
# print(translator.spanish_translator("blue"))
# # translator.hungarian_translator("difficult situation")

