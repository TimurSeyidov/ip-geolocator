import os
from dotenv import load_dotenv
from core.interface import LocatorInterface, CacheInterface
from core.component import HttpClient
from core.base import Ip, Location
from core.service import ChainLocator, IpGeoLocationLocator, IpInfoLocator


class Application(LocatorInterface):
    __locator: LocatorInterface = None
    __cache: CacheInterface = None

    def __init__(self, env_file: str, cache: CacheInterface = None):
        file_env = os.path.abspath(env_file)
        self.__cache = cache
        if not os.path.exists(file_env):
            return
        load_dotenv(file_env)
        locators = list()
        ipgeolocation_key = os.getenv('ipgeolocation_key')
        ipinfo_key = os.getenv('ipinfo_key')
        if ipgeolocation_key:
            locators.append(IpGeoLocationLocator(HttpClient(), ipgeolocation_key))
        if ipinfo_key:
            locators.append(IpInfoLocator(HttpClient(), ipinfo_key))
        if len(locators):
            self.__locator = ChainLocator(*locators)

    def locate(self, ip: Ip) -> Location | None:
        if not self.__locator:
            return None
        return self.__locator.locate(ip)

