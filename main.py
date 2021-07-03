import json
import requests
from settings import *
from google.cloud import translate_v2 as translate

translate_client = translate.Client()


def do_post(request):
    username = request.form.get('username')  # type: str
    text = request.form.get('text')  # type: str
    print("username=" + username)
    print("text=" + text)

    display_data = get_settings(user_name)
    print(display_data)
    if display_data is None:
        return "translate"

    if text[0] == "@":  # メンションを除外
        return "translate"

    # if text[:2] == "RT":  # リツイートを除外
    #     return "translate"

    # 翻訳
    translate_result = translate_client.translate(text, target_language="ja")
    translated_text = translate_result['translatedText']  # type: str
    print(translated_text)

    data = {  # type: dict
        "text": "{} *{}*\n{}".format(display_data["icon_name"], user_name, translated_text),
        "unfurl_links": "true",
    }
    payload = json.dumps(data).encode("utf-8")  # type: json
    response = requests.post(SLACK_WEBHOOK_URL, payload)
    print(response)
    return "translate"
