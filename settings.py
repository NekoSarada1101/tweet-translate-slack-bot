SLACK_WEBHOOK_URL = "SLACK_WEBHOOK_URL"
DISPLAY_DATA = [
    {
        "user_name": "user_name1",
        "icon_name": "icon_name1"
    },
    {
        "user_name": "user_name2",
        "icon_name": "icon_name2"
    },
    {
        "user_name": "user_name3",
        "icon_name": "icon_name3"
    },
]


# アカウントごとにSlackWebhookURLとアイコンを設定する
def get_settings(user_name: str):
    for data in DISPLAY_DATA:
        if data["user_name"] == user_name:
            return data
