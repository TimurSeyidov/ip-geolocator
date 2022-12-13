from core.interface import LocatorInterface
from core import Ip, Location, HttpClient


class IpInfoLocator(LocatorInterface):
    __key: str = None
    __client: HttpClient = None

    def __init__(self, client: HttpClient, api_key: str):
        super().__init__()
        self.__key = api_key
        self.__client = client

    def locate(self, ip: Ip) -> Location | None:
        url = 'https://ipinfo.io/' + ip.value
        params = {
            'token': self.__key
        }
        response = self.__client.get(url, params)
        if not response.get('country'):
            return None
        latlng = response.get('loc', '').split(',')
        coord = None
        if len(latlng) == 2:
            coord = tuple([float(x) for x in latlng])
        return Location(
            country=response.get('country'),
            region=response.get('region'),
            city=response.get('city'),
            coord=coord,
            zip=response.get('postal')
        )


