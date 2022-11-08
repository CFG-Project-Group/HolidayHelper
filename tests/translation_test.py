from unittest import TestCase, main
from api.google_translate import translation
from google.cloud import translate_v2
import os
from config import translate_key


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'GoogleKey.json'
translate_client = translate_v2.Client()

object_1 = translation("en", "ahoj")
object_2 = translation("es", "hello")
object_3 = translation("hu", "okay")
object_4 = translation("es", "ahoj")


class TestTranslationResponse(TestCase):

    def test_translation_key(self):
        self.translate_client = translate_v2.Client()
        target_lan = "es"
        output = self.translate_client.translate("hi", target_language=target_lan)
        self.assertEqual(list(output.keys()), ['translatedText', 'detectedSourceLanguage', 'input'])
#
class TestTranslator(TestCase):

    def test_translation_with_valid_input(self):
        self.translate_client = translate_v2.Client()
        self.assertEqual(object_1, {'translatedText': 'Hi', 'detectedSourceLanguage': 'cs', 'input': 'ahoj'})
        self.assertEqual(object_2, {'translatedText': 'Hola', 'detectedSourceLanguage': 'en', 'input': 'hello'})
        self.assertEqual(object_3, {'translatedText': 'oké', 'detectedSourceLanguage': 'en', 'input': 'okay'})
        self.assertEqual(object_4,{'translatedText': 'Hola', 'detectedSourceLanguage': 'cs', 'input': 'ahoj'})

    #
    def test_translation_with_invalid_input(self):
        with self.assertRaises(NameError):
            translation("es", hi)


if __name__ == '__main__':
    main()