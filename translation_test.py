from unittest import TestCase, main
import Google_Translate
from google.cloud import translate_v2
import os


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'GoogleKey.json'
translate_client = translate_v2.Client()

object1 = Google_Translate.Translator()


class TestTranslationResponse(TestCase):

    def test_spanish_translation_key(self):
        self.translate_client = translate_v2.Client()
        target = "es"
        output = self.translate_client.translate("hi", target_language=target)
        self.assertEqual(list(output.keys()), ['translatedText', 'detectedSourceLanguage', 'input'])

class TestTranslator(TestCase):

    def test_czech_translation_with_valid_input(self):
        self.assertEqual(object1.czech_translator("hi"), "ahoj")
        self.assertEqual(object1.czech_translator("cold"), "studený")
        self.assertEqual(object1.czech_translator("sweet"), "bonbón")

    def test_czech_translation_with_invalid_input(self):
        with self.assertRaises(TypeError):
            object1.czech_translator(['hi'])

    def test_spanish_translation_with_valid_input(self):
        self.assertEqual(object1.spanish_translator('beautiful'), 'hermoso')
        self.assertEqual(object1.spanish_translator('hello'), 'hola')
        self.assertEqual(object1.spanish_translator('blue'), 'azul')

    def test_spanish_translation_with_invalid_input(self):
        with self.assertRaises(TypeError):
            object1.spanish_translator(['hi'])

    def test_hungarian_translation_with_valid_input(self):
        self.assertEqual(object1.hungarian_translator('cut'), 'vágott')
        self.assertEqual(object1.hungarian_translator('cute'), 'aranyos')
        self.assertEqual(object1.hungarian_translator('girl'), 'lány')


if __name__ == '__main__':
    main()