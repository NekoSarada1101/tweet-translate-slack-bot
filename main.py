import json
import requests
from settings import *
from google.cloud import translate_v2 as translate

translate_client = translate.Client.from_service_account_json("credentials.json")


def do_post(request):
    text = request.form.get('text')  # type: str
    username = request.form.get('username')  # type: str

    print("text={}, username={}".format(text, username))

    # 翻訳
    result = translate_client.translate(text, target_language="ja")
    translated_text = result['translatedText']  # type: str
    print(translated_text)

    result = set_settings(username)
    print(result)

    data = {  # type: dict
        "text": "{} *{}*\n{}".format(result[1], username, translated_text),
        "unfurl_links": "true",
    }
    payload = json.dumps(data).encode("utf-8")  # type: json
    response = requests.post(result[0], payload)
    print(response)
