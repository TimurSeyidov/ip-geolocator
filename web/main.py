import os
from flask import Flask, render_template, request
from core.base import Ip
from core import BaseApplication
from core.component import FileCache

if __name__ == '__main__':
    app = BaseApplication(
        env_file='../.env'
    )
    app.cache = FileCache(os.path.abspath(app.get_config('cache_path', '../cache')))
    webapp = Flask(
        __name__,
        template_folder=os.path.abspath('./template'),
        static_folder=os.path.abspath('./template/static')
    )

    @webapp.errorhandler(404)
    def page_not_found(e):
        return render_template('error.html'), 404

    @webapp.get('/')
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
    webapp.run(
        host=app.get_config('web_host', '0.0.0.0'),
        port=app.get_config('web_port', 4000)
    )


