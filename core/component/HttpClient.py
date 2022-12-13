import requests
from typing import Dict


class HttpClient:
    def get(self, url: str, params: Dict | None = None):
        response = requests.get(url, params)
        return response.json()

