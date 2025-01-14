import os
import requests
from datetime import datetime

class TelegramChannel():
    def __init__(self):
        self.token = os.getenv("TELEGRAM_TOKEN")
        self.chat_id = os.getenv("CHAT_ID")

    def send_message(self, text):
        url = f"https://api.telegram.org/bot{self.token}/sendMessage?chat_id={self.chat_id}&text={text}&amp;parse_mode=MarkdownV2"
        response = requests.post(url).json()
        
        if not response.get("ok"):
            return "Failed to send message"
        return "Message sent successfully on Telegram"

    def receive_messages(self, after_timestamp):
        url = f"https://api.telegram.org/bot{self.token}/getUpdates"
        response = requests.get(url).json()
        if not response.get("result"):
            return []

        new_messages = []
        for update in response["result"]:
            if "message" in update:
                message = update["message"]
                if message["date"] > after_timestamp:
                    new_messages.append({
                        "text": message["text"],
                        "date": datetime.fromtimestamp(message["date"]).strftime("%Y-%m-%d %H:%M")
                    })

        return new_messages