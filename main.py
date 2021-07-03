import json
import requests
from settings import *
from google.cloud import translate_v2 as translate

translate_client = translate.Client()


def do_post(request):
    username = request.form.get('username')  # type: str
    image = request.form.get('image')  # type: str
    text = request.form.get('text')  # type: str
    mention = request.form.get('mention')  # type: str
    print("username=" + username)
    print("image=" + image)
    print("text=" + text)
    print("mention=" + mention)

    display_data = get_settings(user_name)
    print(display_data)
    if display_data is None:
    if mention == "false" and text[0] == "@":  # メンションを除外
        return "translate"

        return "translate"

    # if text[:2] == "RT":  # リツイートを除外
    #     return "translate"

    # 翻訳
    translate_result = translate_client.translate(text, target_language="ja")
    translated_text = translate_result['translatedText']  # type: str
    print(translated_text)

    data = {  # type: dict
        "text": "{} *{}*\n{}".format(image, username, translated_text),
        "unfurl_links": "true",
    }
    payload = json.dumps(data).encode("utf-8")  # type: json
    response = requests.post(SLACK_WEBHOOK_URL, payload)
    print(response)
    return "translate"
