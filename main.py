import json
import requests
from settings import *
from google.cloud import translate_v2 as translate

translate_client = translate.Client()


def do_post(request):
    text = request.form.get('text')  # type: str
    username = request.form.get('username')  # type: str

    print("text={}, username={}".format(text, username))

    result = set_settings(username)
    print(result)
    if result[0] == "" or result[1] == "":
        return

    if text[0] == "@":  # メンションなら
        return

    # 翻訳
    translate_result = translate_client.translate(text, target_language="ja")
    translated_text = translate_result['translatedText']  # type: str
    print(translated_text)

    data = {  # type: dict
        "text": "{} *{}*\n{}".format(result[1], username, translated_text),
        "unfurl_links": "true",
    }
    payload = json.dumps(data).encode("utf-8")  # type: json
    response = requests.post(result[0], payload)
    print(response)
    return "translate"
