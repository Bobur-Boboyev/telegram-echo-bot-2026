import time
import requests
from config import TOKEN


class EchoBot:
    def __init__(self, token: str):
        self.BASE_URL = f"https://api.telegram.org/bot{token}"
        self.offset = None

    def get_updates(self):
        url = f"{self.BASE_URL}/getUpdates"
        params = {
            "offset": self.offset,
            "limit": 10
        }
        response = requests.get(url, params=params)
        return response.json()["result"]

    def send(self, method: str, chat_id: int, file_id: str = None, text: str = None):
        url = f"{self.BASE_URL}/{method}"
        data = {"chat_id": chat_id}
        if text:
            data["text"] = text
        if file_id:
            data[method.replace("send", "").lower()] = file_id
        requests.post(url, data=data)

    def start_polling(self):

        while True:
            updates = self.get_updates()
            time.sleep(1)

            for update in updates:
                message = update.get("message")
                if not message:
                    continue

                chat_id = message["chat"]["id"]

                if "text" in message:
                    self.send("sendMessage", chat_id, text=message["text"])

                if "photo" in message:
                    self.send("sendPhoto", chat_id, file_id=message["photo"][-1]["file_id"])

                if "audio" in message:
                    self.send("sendAudio", chat_id, file_id=message["audio"]["file_id"])

                if "document" in message:
                    self.send("sendDocument", chat_id, file_id=message["document"]["file_id"])

                if "video" in message:
                    self.send("sendVideo", chat_id, file_id=message["video"]["file_id"])

                if "animation" in message:
                    self.send("sendAnimation", chat_id, file_id=message["animation"]["file_id"])

                if "voice" in message:
                    self.send("sendVoice", chat_id, file_id=message["voice"]["file_id"])

                self.offset = update["update_id"] + 1


bot = EchoBot(TOKEN)
bot.start_polling()
