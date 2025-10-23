import requests
import os
from dotenv import load_dotenv


load_dotenv()


class Notify:

    def __init__(self):
        self.__base_url = 'https://webhook.site'
        self.__api_key = os.getenv('WEBHOOK_API_KEY')

    def send_order_event(self, data):
        requests.post(
            url=f'{self.__base_url}/{self.__api_key}',
            json=data,
        )
