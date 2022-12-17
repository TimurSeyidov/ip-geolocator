import os
from typing import Any
from dotenv import load_dotenv
from core.interface import LocatorInterface, CacheInterface
from core.component import HttpClient
from core.base import Ip, Location
from core.service import ChainLocator, IpGeoLocationLocator, IpInfoLocator, Ip2MeLocator


class Application(LocatorInterface):
    __locator: LocatorInterface = None
    __cache: CacheInterface = None

    def __init__(self, env_file: str, cache: CacheInterface = None):
        file_env = os.path.abspath(env_file)
        self.__cache = cache
        if not os.path.exists(file_env):
            return
        load_dotenv(file_env)
        locators = [
            Ip2MeLocator(HttpClient())
        ]
        ipgeolocation_key = os.getenv('ipgeolocation_key')
        ipinfo_key = os.getenv('ipinfo_key')
        if ipgeolocation_key:
            locators.append(IpGeoLocationLocator(HttpClient(), ipgeolocation_key))
        if ipinfo_key:
            locators.append(IpInfoLocator(HttpClient(), ipinfo_key))
        if len(locators):
            self.__locator = ChainLocator(*locators)

    def locate(self, ip: Ip) -> Location | None:
        if self.__cache:
            location = self.__cache.get(ip.value)
            if location:
                return Location(
                    country=location.get('country'),
                    region=location.get('region'),
                    zip=location.get('zip'),
                    city=location.get('city'),
                    coord=(location.get('lat'), location.get('lng'))
                )
        if not self.__locator:
            return None
        result = self.__locator.locate(ip)
        if self.__cache and result:
            self.__cache.set(ip.value, result.dict, 120)
        return result

    @property
    def cache(self) -> CacheInterface | None:
        return self.__cache

    @cache.setter
    def cache(self, cache: CacheInterface):
        self.__cache = cache

    @staticmethod
    def get_config(key: str, default: Any = None) -> Any:
        return os.getenv(key, default)

