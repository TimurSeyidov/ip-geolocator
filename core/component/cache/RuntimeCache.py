from typing import Dict, List
from core.interface import CacheInterface
import datetime as dt


class RuntimeCache(CacheInterface):
    __values: Dict = Dict

    def __init__(self):
        super().__init__()
        self.__values = dict()

    def get(self, key: str) -> str | int | float | None:
        if key not in self.__values:
            return None
        value = self.__values.get(key, dict())
        if not value.get('ttl'):
            return value.get('value')
        ttl = value.get('ttl')
        last_time = value.get('time')
        current_time = dt.datetime.now()
        if (current_time - last_time).total_seconds() > ttl:
            return None
        return value.get('value')

    def set(self, key: str, value: str | int | float | List | Dict = None, ttl: int = 0):
        self.__values[key] = {
            'ttl': ttl,
            'time': dt.datetime.now(),
            'value': value
        }

