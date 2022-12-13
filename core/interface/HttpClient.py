from abc import ABCMeta, abstractmethod
from typing import Dict, Any


class HttpClient:
    __metaclass__ = ABCMeta

    @abstractmethod
    def get(self, url: str, params: Dict | None = None) -> Any:
        pass

