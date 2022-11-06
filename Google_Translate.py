import os
from google.cloud import translate_v2
import requests

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'GoogleKey.json'

# text = input("input: ")
translate_client = translate_v2.Client()

def translation(target_lan, text):
    output = translate_client.translate(text, target_language=target_lan)
    return output

#choosing spanish as an example

if __name__ == '__main__':
    # translator = Translator(text)
    print(translation("es", 'hello'))
