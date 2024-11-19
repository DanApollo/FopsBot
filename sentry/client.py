import requests

from utils import format

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
                return format(feedback_data[1])
            else:
                return None
        else:
            print(f"Error retrieving user feedback: {response.status_code}")
            return None

sentry_client = SentryClient()