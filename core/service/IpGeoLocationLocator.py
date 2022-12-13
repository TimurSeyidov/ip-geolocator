from core.interface import LocatorInterface
from core import Ip, Location, HttpClient


class IpGeoLocationLocator(LocatorInterface):
    __key: str = None
    __client: HttpClient = None

    def __init__(self, client: HttpClient, api_key: str):
        super().__init__()
        self.__key = api_key
        self.__client = client

    def locate(self, ip: Ip) -> Location | None:
        url = 'https://api.ipgeolocation.io/ipgeo'
        params = {
            'ip': ip.value,
            'apiKey': self.__key
        }
        response = self.__client.get(url, params)
        if not response.get('country_name'):
            return None
        lat = response.get('latitude')
        lng = response.get('longitude')
        coord = None
        if lat and lng:
            coord = (float(lat), float(lng))
        return Location(
            country=response.get('country_name'),
            region=response.get('state_prov'),
            city=response.get('city'),
            coord=coord,
            zip=response.get('zipcode')
        )



