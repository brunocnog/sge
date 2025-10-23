import requests


class Notify:

    def __init__(self):
        self.__base_url = 'https://webhook.site'

    def send_event(self, data):
        requests.post(
            url=f'{self.__base_url}/e45162e6-2852-41fc-93b9-fee461f6c6d7',
            json=data,
        )
