import requests

BOT_TOKEN = '*******************'
CHAT_ID = '********'

def send_alert(message):
    """Sends a message to the specified Telegram chat."""
    url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
    payload = {'chat_id': CHAT_ID, 'text': message}

    try:
        response = requests.post(url, data=payload)
        response.raise_for_status()
        print(f"Telegram alert sent: {message}")
    except requests.exceptions.RequestException as e:
        print(f"Error sending Telegram alert: {e}")