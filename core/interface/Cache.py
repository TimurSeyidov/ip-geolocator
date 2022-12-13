from abc import ABCMeta, abstractmethod


class Cache:
    __metaclass__ = ABCMeta

    @abstractmethod
    def get(self, key: str) -> str | int | float | None:
        pass

    @abstractmethod
    def set(self, key: str, value: str | int | float = None, ttl: int = 0):
        pass
