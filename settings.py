SLACK_WEBHOOK_URL = ""
ICON_NAME = ""


# アカウントごとにSlackWebhookURLとアイコンを設定する
def set_settings(username: str):
    if username == "username1":
        SLACK_WEBHOOK_URL = "SLACK_WEBHOOK_URL1"
        ICON_NAME = "ICON_NAME1"
    elif username == "username2":
        SLACK_WEBHOOK_URL = "SLACK_WEBHOOK_URL2"
        ICON_NAME = "ICON_NAME2"
    elif username == "username3":
        SLACK_WEBHOOK_URL = "SLACK_WEBHOOK_URL3"
        ICON_NAME = "ICON_NAME3"
    print(SLACK_WEBHOOK_URL)
    print(ICON_NAME)
