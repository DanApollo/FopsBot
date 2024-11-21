import re

def handle_mentions(body, say, client, gemini_client, sentry_client):
    result = client.auth_test()["user_id"]
    text = body["event"]["text"]
    cleaned_text = re.sub(f"<@{result}>", "", text).strip()
    if cleaned_text == "last week":
        fake_last_week(say, gemini_client, sentry_client)
    else:
        respond(say, cleaned_text, gemini_client)

def last_post(say, sentry_client):
    response = sentry_client.get_last_user_feedback()
    if response:
        say(response)

def fake_last_week(say, gemini_client, sentry_client):
    input_data = sentry_client.get_fake_last_week_user_feedback()
    if input_data:
        response = gemini_client.generate_response(input_data)
        say(response)

def respond(say, cleaned_text, gemini_client):
    response = gemini_client.generate_response(cleaned_text)
    say(response)