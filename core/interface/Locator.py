from abc import ABCMeta, abstractmethod
from core.base import Ip, Location



class Locator:
    __metaclass__ = ABCMeta

    @abstractmethod
    def locate(self, ip: Ip) -> Location | None:
        pass
