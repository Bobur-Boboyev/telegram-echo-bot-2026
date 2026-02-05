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
        return requests.get(url, params=params).json()["result"]

    def send(self, method: str, chat_id: int, **kwargs):
        url = f"{self.BASE_URL}/{method}"
        data = {"chat_id": chat_id}
        data.update(kwargs)
        requests.get(url, data=data)

    def start_polling(self):

        while True:
            updates = self.get_updates()

            for update in updates:
                message = update.get("message")
                if not message:
                    continue

                chat_id = message["chat"]["id"]

                if "text" in message:
                    self.send("sendMessage", chat_id, text=message["text"])

                elif "photo" in message:
                    self.send("sendPhoto", chat_id, photo=message["photo"][-1]["file_id"])

                elif "audio" in message:
                    self.send("sendAudio", chat_id, audio=message["audio"]["file_id"])

                elif "document" in message:
                    self.send("sendDocument", chat_id, document=message["document"]["file_id"])

                elif "video" in message:
                    self.send("sendVideo", chat_id, video=message["video"]["file_id"])

                elif "animation" in message:
                    self.send("sendAnimation", chat_id, animation=message["animation"]["file_id"])

                elif "voice" in message:
                    self.send("sendVoice", chat_id, voice=message["voice"]["file_id"])

                elif "video_note" in message:
                    self.send("sendVideoNote", chat_id, video_note=message["video_note"]["file_id"])

                elif "location" in message:
                    loc = message["location"]
                    self.send(
                        "sendLocation",
                        chat_id,
                        latitude=loc["latitude"],
                        longitude=loc["longitude"]
                    )

                elif "venue" in message:
                    v = message["venue"]
                    self.send(
                        "sendVenue",
                        chat_id,
                        latitude=v["location"]["latitude"],
                        longitude=v["location"]["longitude"],
                        title=v["title"],
                        address=v["address"]
                    )

                elif "contact" in message:
                    c = message["contact"]
                    self.send(
                        "sendContact",
                        chat_id,
                        phone_number=c["phone_number"],
                        first_name=c["first_name"]
                    )

                elif "poll" in message:
                    p = message["poll"]
                    options = [o["text"] for o in p["options"]]
                    self.send(
                        "sendPoll",
                        chat_id,
                        question=p["question"],
                        options=options
                    )

                elif "dice" in message:
                    self.send("sendDice", chat_id)

                self.offset = update["update_id"] + 1


bot = EchoBot(TOKEN)
bot.start_polling()

