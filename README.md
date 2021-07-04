# tweet-translate-slack-bot

<img width="300" src="https://user-images.githubusercontent.com/46714670/107322576-0f80fa80-6ae8-11eb-89d5-4696084b7351.png"> <img width="480" src="https://user-images.githubusercontent.com/46714670/107322562-05f79280-6ae8-11eb-878b-7c62da600e19.png">

### 概要

英語のツイートを日本語に翻訳してSlackで表示する。

### 開発環境

* Python 3.8
* [Translation API](https://cloud.google.com/translate?hl=ja)
* [Cloud Functions](https://cloud.google.com/functions?hl=ja)
* [IFTTT](https://ifttt.com)

### 使用方法

1. リポジトリをクローンする。
   ```bash
   git clone https://github.com/NekoSarada1101/tweet-translate-slack-bot.git
   ```

2. GCPでCloud Translation APIを有効にする。

3. Cloud Functionsにデプロイする。
    ```bash
    gcloud functions deploy [NAME] --region [REGION] --entry-point do_post --runtime python38 --trigger-http --allow-unauthenticated
    ```

4. デプロイ時に出力される`httpsTrigger`のURLを保存する。
   ```bash
   httpsTrigger:
     securityLevel: SECURE_OPTIONAL
     url: https://[REGION]-[PROJECT-NAME].cloudfunctions.net/[NAME] ←this
   ```

5. IFTTTでAppletsを作成する。  
   <img width="500" src="https://user-images.githubusercontent.com/46714670/124374329-4e9d2b80-dcd5-11eb-8ec6-a6c6b947b1c9.png">

   * username : 表示する名前
   * image : 表示する絵文字の名前
   * text : 翻訳するテキスト
   * mention : メンションを表示するならtrue、しないならfalse
   * retweet : リツイートを表示するならtrue、しないならfalse

### ライセンス

[MIT](https://github.com/NekoSarada1101/tweet-translate-slack-bot/blob/main/LICENSE)
