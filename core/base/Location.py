from typing import Tuple, Dict


class Location:
    __country: str | None = None
    __city: str | None = None
    __region: str | None = None
    __lat: float = None
    __lng: float = None
    __zip: str = None

    __fields = ['country', 'region', 'city', 'lat', 'lng', 'zip']

    def __init__(self,
                 country: str,
                 region: str | None = None,
                 city: str | None = None,
                 coord: Tuple[float, float] = None,
                 zip: str = None
                 ):
        country = country.strip()
        if region:
            region = region.strip()
        if city:
            city = city.strip()
        if zip:
            zip = zip.strip()
        if not country:
            raise ValueError('Empty country')
        self.__country = country
        self.__region = region
        self.__city = city
        self.__zip = zip
        if coord:
            self.__lat, self.__lng = coord

    @property
    def country(self) -> str | None:
        return self.__country

    @property
    def region(self) -> str | None:
        return self.__region

    @property
    def city(self) -> str | None:
        return self.__city

    @property
    def lat(self) -> float | None:
        return self.__lat

    @property
    def lng(self) -> float | None:
        return self.__lng

    @property
    def latlng(self) -> Tuple[float, float] | None:
        return (self.lat, self.lng) if self.lat else None

    @property
    def zip(self) -> str | None:
        return self.__zip

    def __str__(self):
        result = list()
        for key in self.__fields:
            value = getattr(self, key)
            if value:
                result.append(f'{key.capitalize()}: {value}')
        return '; '.join(result)

    @property
    def weight(self) -> Tuple[int, int]:
        total = len(self.__fields)
        filled = 0
        for key in self.__fields:
            value = getattr(self, key)
            if value:
                filled += 1
        return filled, total

    @property
    def dict(self) -> Dict:
        result = dict()
        for key in self.__fields:
            result[key] = getattr(self, key)
        return result
