import os
from dotenv import load_dotenv

load_dotenv()

# Sentry configuration
SENTRY_SECRET = os.environ.get("SENTRY_SECRET")
SENTRY_DSN = os.environ.get("SENTRY_DSN")