class Location:
    __country: str | None = None
    __city: str | None = None
    __region: str | None = None

    def __init__(self, country: str, region: str | None = None, city: str | None = None):
        country = country.strip()
        if region:
            region = region.strip()
        if city:
            city = city.strip()
        if not country:
            raise ValueError('Empty country')
        self.__country = country
        self.__region = region
        self.__city = city

    @property
    def country(self) -> str | None:
        return self.__country

    @property
    def region(self) -> str | None:
        return self.__region

    @property
    def city(self) -> str | None:
        return self.__city
