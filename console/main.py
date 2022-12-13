import sys
from core.base import Ip
from core import BaseApplication

if __name__ == '__main__':
    ip_address = input('Enter IP address: ').strip()
    if not ip_address:
        print('IP address is empty')
        sys.exit()
    app = BaseApplication(env_file='../.env')
    result = app.locate(Ip(ip_address))
    print(result)


