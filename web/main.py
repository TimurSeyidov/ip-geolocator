import os
from flask import Flask, render_template, request
from core.base import Ip
from core import BaseApplication
from core.component import RuntimeCache

if __name__ == '__main__':
    app = BaseApplication(
        env_file='../.env',
        cache=RuntimeCache()
    )
    webapp = Flask(
        __name__,
        template_folder=os.path.abspath('./template'),
        static_folder=os.path.abspath('./template/static')
    )

    @webapp.get('/')
    @webapp.get('/<ip>')
    def index():
        location = dict()
        args = request.args
        ip = args.get('ip', '').strip()
        if ip:
            find = app.locate(Ip(ip))
            if find:
                location = find.dict
        yandex_js_api_key = app.get_config('yandex_js_api_key')
        return render_template("index.html", ip=args.get('ip', ''), yandex_js_api_key=yandex_js_api_key, **location)

    webapp.run('127.0.0.1', 3001)


