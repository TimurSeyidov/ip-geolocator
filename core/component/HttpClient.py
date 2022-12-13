import requests
from typing import Dict
from core.interface import HttpClientInterface


class HttpClient(HttpClientInterface):
    def get(self, url: str, params: Dict | None = None):
        response = requests.get(url, params)
        return response.json()
