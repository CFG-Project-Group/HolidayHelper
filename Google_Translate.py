import os
from google.cloud import translate_v2




os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"GoogleKey.json"


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


translator = Translator()

#choosing spanish as an example

if __name__ == '__main__':
    print(translator.spanish_translator("blue"))