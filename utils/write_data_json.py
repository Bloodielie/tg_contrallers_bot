from .json import JsonWrite
from .validation import BusStopCheck, BusStopGet
from config import JSON_BUS_STOP, JSON_BUS_STOP_CLEAN
import asyncio


class WriteBusStop:
    def __init__(self, vk):
        self.vk = vk

    def write_dirty_post(self):
        """ Функция для записи данных о грязных остановках в файл """
        bus_check = BusStopCheck()
        bus_get = BusStopGet(self.vk)
        dates = bus_check.validation_bus_stop(bus_check.cleaning_post(bus_get.get_post_un_time()))

        _dict = {}
        for data in dates:
            _dict.update({int(data[1]): data[0]})

        JsonWrite(JSON_BUS_STOP).write_json_unsafe(_dict)

    def write_clean_post(self):
        """ Функция для записи данных о чистых остановках в файл """
        bus_check = BusStopCheck()
        bus_get = BusStopGet(self.vk)
        dates = bus_check.validation_bus_stop(bus_check.cleaning_post_otherwise(bus_get.get_post_un_time()))

        _dict = {}
        for data in dates:
            _dict.update({int(data[1]): data[0]})

        JsonWrite(JSON_BUS_STOP_CLEAN).write_json_unsafe(_dict)

    async def on_task_write(self, time):
        self.write_dirty_post()
        self.write_clean_post()
        await asyncio.sleep(time)
