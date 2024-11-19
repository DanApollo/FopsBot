import re

def handle_mentions(body, say, client, gemini_client, sentry_client):
    result = client.auth_test()["user_id"]
    user_id = body["event"]["user"]
    text = body["event"]["text"]
    cleaned_text = re.sub(f"<@{result}>", "", text).strip() 
    if cleaned_text == "last":
        input_data = sentry_client.get_last_user_feedback()
        if input_data:
            response = input_data
            say(response)
    elif cleaned_text == "last week":
        input_data = sentry_client.get_last_week_user_feedback()
        if input_data:
            response = gemini_client.generate_response(input_data)
            say(response)