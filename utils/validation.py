from .json import JsonWrite
from time import time
from config import JSON_BUS, JSON_TROLLEYBUSES


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

    temporary_lists = []
    for stop in _bus_stop:
        for _data in data:
            if _data[0] == stop.lower():
                t = (_data[0], [_data[1][0], _data[1][1]])
                temporary_lists.append(t)
    return temporary_lists
