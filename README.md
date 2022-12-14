IP Geolocator
=============

Данный проект разрабытавался в академических целях. Основной упор делается на разделение классов, использование типов в Python, разработку независемых компонентов

Технические требования
----------------------

Python версии 3.10+

Установка
---------

Все зависимости указаны в файле **requirements.txt**. Необходимо поднять виртуальное окружение и поставить все зависимости из файла

Настройка
---------

Данный геолокатор может работать с сервисами **IpGeolocation**, **Ip2Me** и **IpInfo**. При желании можно добавить свои сервисы, реализовав интерфейс **Locator**

Необходимо создать в корне файл **.env** (пример лежит в **default.env) и прописать настройки сервисов**. Также можно подключить api ключ от Яндекса для отображения карты

*   [IpGeolocation](https://ipgeolocation.io)
*   [IpInfo](https://ipinfo.io/)
*   [Ключ Яндекса](https://yandex.ru/dev/maps/jsapi/doc/2.1/quick-start/index.html?from=jsapi)

Консольное приложение
---------------------

В папке **console** в файл **main.py** реализовано консольное приложение по определению IP

Веб приложение
--------------

В папке **web** в файл **main.py** реализовано консольное приложение по определению IP

Тесты
-----

В папке **test** лежат файлы для тестирования базовых компонентов
