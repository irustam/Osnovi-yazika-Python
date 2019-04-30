
"""
== OpenWeatherMap ==

OpenWeatherMap — онлайн-сервис, который предоставляет бесплатный API
 для доступа к данным о текущей погоде, прогнозам, для web-сервисов
 и мобильных приложений. Архивные данные доступны только на коммерческой основе.
 В качестве источника данных используются официальные метеорологические службы
 данные из метеостанций аэропортов, и данные с частных метеостанций.

Необходимо решить следующие задачи:

== Получение APPID ==
    Чтобы получать данные о погоде необходимо получить бесплатный APPID.

    Предлагается 2 варианта (по желанию):
    - получить APPID вручную
    - автоматизировать процесс получения APPID,
    используя дополнительную библиотеку GRAB (pip install grab)

        Необходимо зарегистрироваться на сайте openweathermap.org:
        https://home.openweathermap.org/users/sign_up

        Войти на сайт по ссылке:
        https://home.openweathermap.org/users/sign_in

        Свой ключ "вытащить" со страницы отсюда:
        https://home.openweathermap.org/api_keys

        Ключ имеет смысл сохранить в локальный файл, например, "app.id"


== Получение списка городов ==
    Список городов может быть получен по ссылке:
    http://bulk.openweathermap.org/sample/city.list.json.gz

    Далее снова есть несколько вариантов (по желанию):
    - скачать и распаковать список вручную
    - автоматизировать скачивание (ulrlib) и распаковку списка
     (воспользоваться модулем gzip
      или распаковать внешним архиватором, воспользовавшись модулем subprocess)

    Список достаточно большой. Представляет собой JSON-строки:
{"_id":707860,"name":"Hurzuf","country":"UA","coord":{"lon":34.283333,"lat":44.549999}}
{"_id":519188,"name":"Novinki","country":"RU","coord":{"lon":37.666668,"lat":55.683334}}


== Получение погоды ==
    На основе списка городов можно делать запрос к сервису по id города. И тут как раз понадобится APPID.
        By city ID
        Examples of API calls:
        http://api.openweathermap.org/data/2.5/weather?id=2172797&appid=b1b15e88fa797225412429c1c50c122a

    Для получения температуры по Цельсию:
    http://api.openweathermap.org/data/2.5/weather?id=520068&units=metric&appid=b1b15e88fa797225412429c1c50c122a

    Для запроса по нескольким городам сразу:
    http://api.openweathermap.org/data/2.5/group?id=524901,703448,2643743&units=metric&appid=b1b15e88fa797225412429c1c50c122a


    Данные о погоде выдаются в JSON-формате
    {"coord":{"lon":38.44,"lat":55.87},
    "weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04n"}],
    "base":"cmc stations","main":{"temp":280.03,"pressure":1006,"humidity":83,
    "temp_min":273.15,"temp_max":284.55},"wind":{"speed":3.08,"deg":265,"gust":7.2},
    "rain":{"3h":0.015},"clouds":{"all":76},"dt":1465156452,
    "sys":{"type":3,"id":57233,"message":0.0024,"country":"RU","sunrise":1465087473,
    "sunset":1465149961},"id":520068,"name":"Noginsk","cod":200}


== Сохранение данных в локальную БД ==
Программа должна позволять:
1. Создавать файл базы данных SQLite со следующей структурой данных
   (если файла базы данных не существует):

    Погода
        id_города           INTEGER PRIMARY KEY
        Город               VARCHAR(255)
        Дата                DATE
        Температура         INTEGER
        id_погоды           INTEGER                 # weather.id из JSON-данных

2. Выводить список стран из файла и предлагать пользователю выбрать страну
(ввиду того, что список городов и стран весьма велик
 имеет смысл запрашивать у пользователя имя города или страны
 и искать данные в списке доступных городов/стран (регуляркой))

3. Скачивать JSON (XML) файлы погоды в городах выбранной страны
4. Парсить последовательно каждый из файлов и добавлять данные о погоде в базу
   данных. Если данные для данного города и данного дня есть в базе - обновить
   температуру в существующей записи.


При повторном запуске скрипта:
- используется уже скачанный файл с городами;
- используется созданная база данных, новые данные добавляются и обновляются.


При работе с XML-файлами:

Доступ к данным в XML-файлах происходит через пространство имен:
<forecast ... xmlns="http://weather.yandex.ru/forecast ...>

Чтобы работать с пространствами имен удобно пользоваться такими функциями:

    # Получим пространство имен из первого тега:
    def gen_ns(tag):
        if tag.startswith('{'):
            ns, tag = tag.split('}')
            return ns[1:]
        else:
            return ''

    tree = ET.parse(f)
    root = tree.getroot()

    # Определим словарь с namespace
    namespaces = {'ns': gen_ns(root.tag)}

    # Ищем по дереву тегов
    for day in root.iterfind('ns:day', namespaces=namespaces):
        ...

"""

import json
import requests
import os
from urllib.request import urlretrieve
import shutil
import gzip
import re

class RegionWeather:
    def __init__(self):
        self.filecitylist = 'city.list.json'

        #Проверяем, есть ли у нас на диске список городов city.list.json. Если нет, то скачиваем и распаковываем:
        if not os.path.isfile(os.path.join('', self.filecitylist)):
            zipfile = self.__filedownload('http://bulk.openweathermap.org/sample/city.list.json.gz', self.filecitylist + '.gz')
            if zipfile:
                if not self.__fileunpack(zipfile):
                    print('Ошибка распаковки файла')
            else:
                print('Ошибка загрузки списка городов')

        #Читаем распакованный файл и записываем в переменную
        self.readcitylist()

    def __filedownload(self, file_url, filename):
        #Функция загрузки файла по урлу file_url и записи в файл с именем filename
        try:
            grab_result = urlretrieve(file_url, filename)
        except:
            return None
        return grab_result[0]

    def __fileunpack(self, zipfile):
        #Функция распаковки gz файла zipfile и записи в файл с именем unpackfile
        with gzip.open(os.path.join('', zipfile), 'rb') as gz_file:
            try:
                self.__openfile(self.filecitylist, 'wb')
                shutil.copyfileobj(gz_file, self.__file)
                self.__closefile()
            except:
                return None
        return True

    def readcitylist(self):
        try:
            self.__openfile(self.filecitylist, 'rb')
            self.citylistdata = json.loads(self.__file.read())
            self.__closefile()
        except FileExistsError:
            return None

    def choose_region(self, region = 'страну', cntry = '.*'):
        #Функция для запроса страны или города у пользователя. Функция возвращает объект - регион, выбранный пользователем
        try:
            newregion = str(input(f'Укажите {region} на английском языке для поиска погоды'))
        except:
            return None

        newregion = self.find_region(newregion, cntry)

        if newregion and region == 'страну':
            return Country(newregion)
        if newregion and region == 'город':
            return City(newregion)
        else:
            return None

    def __specify_region(self, region_list):
        #Функция уточняет выбор пользователя. Она выводит список найденных регионов и просит выбрать регион из списка. Возвращает словаь с выбранным регионом
        for key, itm in enumerate(region_list, 1):
            print(key, itm['name'])
        region_id = int(input('Мы нашли несколько вариантов\nВведите id интересующего региона:'))
        return region_list[region_id-1]

    def city_or_country(self, mycountry):
        #Функция предлагает выбрать пользователю, подтягивать погоду по городу или по всем городам страны. Возвращает объект, по которому нужно подтянуть погоду.
        try:
            userchoose = int(input(f'Где вы хотите узнать погоду? \n1 - во всех городах страны {mycountry.name}, \n2 - выбрать определенный город в стране'))
        except:
            return None

        if userchoose == 1:
            return mycountry
        elif userchoose == 2:
            return self.choose_region('город', mycountry.country)

    def find_region(self, region, cntry = '.*'):
        #Функция для поиска города или страны в файле city.list.json. Функция возвращает словаь с выбранным городом или страной
        result = list(filter(lambda x: re.fullmatch(r'.*%s.*' % region, x['name'], re.IGNORECASE) and re.fullmatch(r'%s' % cntry, x['country']), self.citylistdata))

        if len(result) > 1:
            result = self.__specify_region(result)
            return result
        elif len(result) == 0:
            return None
        else:
            return result[0]

    def __openfile(self, filename, param):
        filename = os.path.join('', filename)
        if os.path.isfile(filename):
            self.__file = open(filename, param)

    def __closefile(self):
        self.__file.close()

    def get_weather(self, region):
        #Создаем и отправляем запрос для указанного региона
        myrequest = requests.get(self.__get_request(region))

        #Записываем результат запроса в БД
        if not os.path.isfile(os.path.join('', 'weather_result')):
            self.__openfile('weather_result', 'w')
        else:
            self.__openfile('weather_result', 'a')

        self.__file.write(myrequest.text)
        self.__closefile()
        return self.__get_request(region)

    def __get_request(self, region):
        #Читаем API ключ из файла
        try:
            self.__openfile('app.id', 'r')
            app_id = self.__file.read()
            self.__closefile()
        except FileExistsError:
            return None

        #Определяем, страна это или город
        if region.regiontype == 'country':
            region_id = region.get_id_all_cities()
        elif region.regiontype == 'city':
            region_id = region.id

        #Формируем запрос погоды по выбранным id
        return f'http://api.openweathermap.org/data/2.5/weather?id={region_id}&appid={app_id}'


class Location:
    def __init__(self, d):
        self.weather = ''

        #Формируем параметры класса из данных пришедшего региона
        for key, value in d.items():
            setattr(self, key, value)

class Country(Location):
    def __init__(self, d):
        Location.__init__(self, d)
        self.regiontype = 'country'

    def get_id_all_cities(self):
        #Функция возвращает список id всех городов в данной стране
        citylist = list(filter(lambda x: x['country'] == self.country, locations.citylistdata))
        return ','.join(map(lambda x: str(x['id']), citylist))

class City(Location):
    def __init__(self, d):
        Location.__init__(self, d)
        self.regiontype = 'city'



locations = RegionWeather()

newcountry = locations.choose_region()

print(newcountry.name)

region = locations.city_or_country(newcountry)

print(region.name, region.id)

print(locations.get_weather(region))

"""
Сделать обработку риквеста
Сделать запись в БД
Сделать чтение и анализ данных в БД
Сделать вывод на экран из БД
"""

"""
locations.readcitylist()
print(locations.citylistdata[0]['name'])

country = list(filter(lambda x: x['country'] == 'GB', locations.citylistdata))
print(country[0])

idlist = list(map(lambda x: x['id'], country))
print(min(idlist))
floc = list(filter(lambda x: x['id'] == min(idlist), country))
print(floc)
"""