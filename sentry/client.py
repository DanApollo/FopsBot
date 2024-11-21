import requests
from datetime import datetime, timedelta, timezone
import json

from utils import most_recent, weekly_report

class SentryClient:
    def __init__(self):
        self.api_key = None
        self.project_slug = None

    def initialize(self, api_key, project_slug):
        self.api_key = api_key
        self.project_slug = project_slug

    def read_json_file(self, file_path):
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
                return data
        except FileNotFoundError:
            print(f"Error: File not found at {file_path}")
            return None
        except json.JSONDecodeError:
            print(f"Error: Invalid JSON format in {file_path}")
            return None

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
        }

        response = requests.get(url, headers=headers)
        response = [event for event in feedback_data if datetime.fromisoformat(event.get('dateCreated').replace('Z', '+00:00')) >= one_week_ago]
        
        if response.status_code == 200:
            feedback_data = response.json()
            if feedback_data:
                return weekly_report(feedback_data)
            else:
                return None
        else:
            print(f"Error retrieving user feedback: {response.status_code}")
            return None
        
    def get_fake_last_week_user_feedback(self):
        one_week_ago = datetime.now(timezone.utc) - timedelta(days=7)
        response = self.read_json_file("./sentry/fakeSentry.json")
        response = [event for event in response if datetime.fromisoformat(event.get('dateCreated').replace('Z', '+00:00')) >= one_week_ago]
        return weekly_report(response)

sentry_client = SentryClient()