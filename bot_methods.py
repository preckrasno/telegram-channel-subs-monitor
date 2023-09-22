# bot_methods.py

import requests
from sentry_sdk import capture_exception

def send_message_to_channel(bot_token, chat_id, message_text):
    """
    Send a message to a specific Telegram channel or chat.

    Parameters:
    - bot_token (str): The token of the Telegram bot.
    - chat_id (str): ID of the chat or channel to send the message to.
    - message_text (str): The content of the message to be sent.
    """
    
    # Base URL for sending a message via the Telegram API
    base_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"

    # Payload with required parameters
    payload = {
        'chat_id': chat_id,
        'text': message_text
    }

    # Make the POST request to send the message
    response = requests.post(base_url, data=payload)

    # Optionally, handle the response to check if the message was sent successfully
    if response.status_code == 200:
        return response.json()
    else:
        # Optionally, raise an error or print the response to debug issues
        response.raise_for_status()
        # send to sentry
        capture_exception(response.raise_for_status())
