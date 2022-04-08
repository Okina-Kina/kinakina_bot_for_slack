import os
import random
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from plugins import Fortune


# ボットトークンと署名シークレットを使ってアプリを初期化します
app = App(token=os.environ.get("SLACK_BOT_TOKEN"))


@app.message("hello")
def message_hello(message, say):
    say(f"hello")


@app.message("占って")
def message_fortune(message, say):
    fortune = Fortune.Fortune().get_fortune_message()
    for m in fortune:
        say(text=m)


@app.action("button_click")
def action_button_click(body, ack, say):
    # アクションを確認したことを即時で応答します
    ack()
    # チャンネルにメッセージを投稿します
    say(f"<@{body['user']['id']}> clicked the button")


# アプリを起動します
if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()
