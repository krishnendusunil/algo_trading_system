import requests

BOT_TOKEN = '8388604051:AAH8YN9mYB_XXNWarvjQvsooVyWNfFO8VuE'
CHAT_ID = '1364769983'

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