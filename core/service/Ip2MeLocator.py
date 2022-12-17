from core.interface import LocatorInterface
from core import Ip, Location, HttpClient


class Ip2MeLocator(LocatorInterface):
    __key: str = None
    __client: HttpClient = None

    def __init__(self, client: HttpClient):
        super().__init__()
        self.__client = client

    def locate(self, ip: Ip) -> Location | None:
        url = 'https://api.2ip.ua/geo.json'
        params = {
            'ip': ip.value
        }
        response = self.__client.get(url, params)
        if not response.get('country'):
            return None
        lat = response.get('latitude')
        lng = response.get('longitude')
        coord = None
        if lat and lng:
            coord = (float(lat), float(lng))
        map = {
            'country': 'country',
            'region': 'region',
            'city': 'city',
            'zip_code': 'zip'
        }
        insert = {
            'coord': coord
        }
        for key, mkey in map.items():
            value = response.get(key + '_rus')
            if not value:
                value = response.get(key)
            insert[mkey] = value
        return Location(**insert)



