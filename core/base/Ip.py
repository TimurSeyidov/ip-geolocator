from ipaddress import ip_address, IPv4Address, IPv6Address


class Ip:
    __value: IPv4Address | IPv6Address | None

    def __init__(self, ip: str):
        ip = ip.strip()
        if not ip:
            raise ValueError('Empty IP')
        try:
            self.__value = ip_address(ip)
        except:
            raise ValueError('Invalid IP ' + ip)

    @property
    def value(self) -> str | None:
        return self.__value.__str__()
