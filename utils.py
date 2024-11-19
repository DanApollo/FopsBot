from datetime import datetime
import textwrap

def wrap_text(text, width=80):
  """Wraps a single line of text to a specified width without breaking words.

  Args:
    text: The text to wrap.
    width: The maximum line width.

  Returns:
    The wrapped text as a string.
  """
  return "\n".join(textwrap.wrap(text, width=width))

def format(data):
    event_id = data.get('event', {}).get('id')

    # Date formatting
    date_created = data.get('dateCreated')
    dt_object = datetime.fromisoformat(date_created.replace('Z', '+00:00'))
    formatted_date = dt_object.strftime("%B %d, %Y at %I:%M %p %Z") 

    email = data.get('email')

    # Wrapping long line of text
    comments = data.get('comments')
    wrapped_comments = wrap_text(comments)

    perma_link = data.get("issue", {}).get('permalink')

    formatted_data = f"""
    *Event ID:* {event_id}
    *Date Created:* {formatted_date}
    *Email:* {email}
    ------------------------------------------------------
    *Comments:*
    {wrapped_comments}
    *Issue URL:* {perma_link}
    ===================================
    """

    # Remove whitespace
    output = "\n".join([line.strip() for line in formatted_data.splitlines()])
    
    return output

def most_recent(data):
    title = "*Most recent Sentry User Feedback Post:*\n"
    leading_string = "==================================="
    output = leading_string + format(data)
    return title + output

def weekly_report(data):
    title = "*Weekly Sentry User Feedback Report:*\n"
    leading_string = "==================================="
    formatted_text = ""
    for obj in data:
        formatted_text += format(obj)
    output = leading_string + formatted_text
    return title + output