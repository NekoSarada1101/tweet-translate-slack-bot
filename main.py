import json
import requests
from settings import SLACK_WEBHOOK_URL
from google.cloud import translate_v2 as translate

translate_client = translate.Client()


def do_post(request):
    username = request.form.get('username')  # type: str
    image = request.form.get('image')  # type: str
    text = request.form.get('text')  # type: str
    mention = request.form.get('mention')  # type: str
    retweet = request.form.get('retweet')  # type: str
    print('username={}, image={}, text={}, mention={}, retweet={}'.format(username, image, text, mention, retweet))

    if mention == "false" and text[0] == "@":  # メンションを除外
        return "translate"

    if retweet == "false" and text[:2] == "RT":  # リツイートを除外
        return "translate"

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
