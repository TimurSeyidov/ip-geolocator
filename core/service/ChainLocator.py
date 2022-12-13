from core.interface import LocatorInterface
from core import Ip, Location
from typing import Tuple


class ChainLocator(LocatorInterface):
    __locators: Tuple[LocatorInterface] | None

    def __init__(self, *args: LocatorInterface):
        super().__init__()
        self.__locators = args

    def locate(self, ip: Ip) -> Location | None:
        location = None
        weight = 0
        for locate in self.__locators:
            l = locate.locate(ip)
            if not l:
                continue
            w, total = l.weight
            if w > weight:
                location = l
                w = weight
        return location



