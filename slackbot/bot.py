from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from .handlers import handle_mentions

def start(slack_bot_token, slack_app_token, gemini_client, sentry_client):
    app = App(token=slack_bot_token)
    handler = SocketModeHandler(app, slack_app_token)

    @app.event("app_mention")
    def handle_app_mentions(body, say, client):
        handle_mentions(body, say, client, gemini_client, sentry_client)

    handler.start()