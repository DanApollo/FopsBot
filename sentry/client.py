import requests
from datetime import datetime, timedelta, timezone

from utils import most_recent, weekly_report

class SentryClient:
    def __init__(self):
        self.api_key = None
        self.project_slug = None

    def initialize(self, api_key, project_slug):
        self.api_key = api_key
        self.project_slug = project_slug

    def get_last_user_feedback(self):
        url = f"https://sentry.io/api/0/organizations/{self.project_slug}/user-feedback/"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            feedback_data = response.json()
            if feedback_data:
                return most_recent(feedback_data[0])
            else:
                return None
        else:
            print(f"Error retrieving user feedback: {response.status_code}")
            return None

    def get_last_week_user_feedback(self):
        one_week_ago = datetime.now(timezone.utc) - timedelta(days=7)
        url = f"https://sentry.io/api/0/organizations/{self.project_slug}/user-feedback/"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "since": one_week_ago.strftime('%Y-%m-%dT%H:%M:%SZ')
        }

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            feedback_data = response.json()
            if feedback_data:
                return weekly_report(feedback_data)
            else:
                return None
        else:
            print(f"Error retrieving user feedback: {response.status_code}")
            return None
sentry_client = SentryClient()