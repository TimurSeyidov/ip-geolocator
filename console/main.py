import sys
import os
from core.base import Ip
from core import BaseApplication
from core.component import FileCache

if __name__ == '__main__':
    ip_address = input('Enter IP address: ').strip()
    if not ip_address:
        print('IP address is empty')
        sys.exit()
    app = BaseApplication(env_file='../.env')
    app.cache = FileCache(os.path.abspath(app.get_config('cache_path', '../cache')))
    try:
        result = app.locate(Ip(ip_address))
        print(result)
    except Exception as e:
        print(e)


