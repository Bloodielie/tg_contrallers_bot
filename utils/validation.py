from .utils import BusStopGet
from config import stop_bus
from datetime import datetime
from .json import JsonWrite
from time import time
from config import JSON_BUS, JSON_TROLLEYBUSES


class BusStopCheck():
    def cleaning_post(self, data: tuple):
        """ Сверка кортежа по определенным словам"""
        for date in data:
            if ('чисто' in date[0]) or ('как' in date[0]) or ('актуально?' in date[0]) or ('cтоят на' in date[0]):
                pass
            else:
                temporary_tuple = (date[0].replace(',', '').replace('\n', '').replace('-', ' ').replace('!', ''), date[1])
                yield temporary_tuple

    def cleaning_post_otherwise(self, data: tuple):
        """ Сверка кортежа по определенным словам"""
        for date in data:
            if 'чисто' in date[0]:
                temporary_tuple = (date[0].replace(',', '').replace('\n', '').replace('-', ' ').replace('!', ''), date[1])
                yield temporary_tuple

    def validation_bus_stop(self, data: tuple):
        """ Поиск остановки в строчке"""
        for _data in data:
            dates = _data[0].split()
            for i in range(len(dates)):
                for j in range(i, len(dates)):
                    combination = ' '.join(dates[i:j + 1])
                    if combination in stop_bus:
                        temporary_tuple = (combination, _data[1])
                        yield temporary_tuple

    def sort_busstop(self, data: tuple, _sort: str = "Время"):
        """ Сортировка генератора по определенному критерию """
        time_data = {}

        for date in data:
            if date[0] not in time_data:
                time_data.update({date[0]: [1, datetime.fromtimestamp(date[1]).strftime('%H:%M')]})
            else:
                _time_data = time_data.get(date[0])
                time_data.update({date[0]: [_time_data[0] + 1, _time_data[1]]})

        if _sort == "Время":
            _sort = 1
        elif _sort == "Сообщения":
            _sort = 0

        return sorted(time_data.items(), key=lambda x: x[1][_sort], reverse=True)


def temporary_list(time_: int, path_file):
    """ Валидация данных файла по ключю """
    hours_back = int(time()) - time_

    data = JsonWrite(path_file).get_json()
    keys = list(data.keys())
    _list = []

    for key in keys:
        if int(key) >= hours_back:
            temporary_tuple = (data.get(key), int(key))
            _list.append(temporary_tuple)
        else:
            break
    return _list


def check_bus(type_bus: str, data, bus_number):
    """ Поиск грязных остановок в остановках автобуса """
    json_utils = JsonWrite(JSON_BUS) if type_bus == 'bus' else JsonWrite(JSON_TROLLEYBUSES)
    _bus_stop = json_utils.get_json().get(bus_number)
    if not _bus_stop:
        return ()

    for stop in _bus_stop:
        for _data in data:
            if _data[0] == stop.lower():
                _tuple = (_data[0], _data[1])
                yield _tuple
