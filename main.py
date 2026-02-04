import requests

from config import TOKEN

BASE_URL = f"https://api.telegram.org/bot{TOKEN}"

class EchoBot:

    def __init__(self, token: str):
        self.BASE_URL = f"https://api.telegram.org/bot{TOKEN}"
        self.offset = None

    def get_updates(self):
        pass

    def send_message(self):
        pass

    def send_photo(self):
        pass

    def send_audio(self):
        pass

    def send_documend(self):
        pass

    def send_video(self):
        pass

    def send_animation(self):
        pass

    def send_animation(self):
        pass

    def send_voice(self):
        pass

    def send_VideoNote(self):
        pass

    def start_polling(self):
        pass


bot = EchoBot(TOKEN)
