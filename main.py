import os
from dotenv import load_dotenv

from slackbot import bot
from sentry import sentry_client
from gemini_cloud import gemini_client

load_dotenv()

sentry_client.initialize(api_key=os.getenv("SENTRY_API_KEY"), project_slug=os.getenv("SENTRY_SLUG"))
gemini_client.initialize(project_id=os.getenv("GCLOUD_PROJECT_ID"))


bot.start(
    slack_bot_token=os.getenv("SLACK_BOT_TOKEN"), 
    slack_app_token=os.getenv("SLACK_APP_TOKEN"),
    gemini_client=gemini_client,
    sentry_client=sentry_client
)