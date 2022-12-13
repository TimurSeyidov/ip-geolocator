from typing import List, Dict
from abc import ABCMeta, abstractmethod


class Cache:
    __metaclass__ = ABCMeta

    @abstractmethod
    def get(self, key: str) -> str | int | float | None:
        pass

    @abstractmethod
    def set(self, key: str, value: str | int | float | List | Dict = None, ttl: int = 0):
        pass
