from utils.json import JsonUtils
from peewee_asyncext import PostgresqlExtDatabase
import peewee_async
import peewee
import asyncio

token = ''
login = ''
password = ''

db_name = 'controller_base'
user = 'postgres'
host = 'localhost'
password_db = 1234


SAVE_DEFAULT_TABLE = 'png/table.gif'
SAVE_DEFAULT_TABLE_CLEAR = 'png/tableclear.gif'
DEFAULT_TABLE = 'png/таблица.png'

DEFAULT_TABLE_BUS = 'png/таблицадляавтобуса.png'
SAVE_DEFAULT_TABLE_BUS = 'png/tablebus.gif'
SAVE_DEFAULT_TABLE_TROLLEYBUSES = 'png/tabletrolleybuses.gif'

JSON_BUS_STOP = "json/temporary_busstop.json"
JSON_BUS_STOP_CLEAN = 'json/temporary_busstop_clean.json'

JSON_BUS = 'json/busstop.json'
JSON_TROLLEYBUSES = 'json/trolleybusesstop.json'

FONT_PNG = 'font/impact.ttf'

stop_bus = JsonUtils('json/stopbus.json').get_json()

MESSAGE = {
    "start_msg": 'Привет! Я Контролер бот для г.Брест.\n Использую клавиатуру ниже чтобы использовать меня.',
    "kontroler_msg": 'Контролеры.',
    "settings_msg": 'Доступные настройки.',
    "menu_msg": 'Главное меню.',
    "kontroler_bus_msg": 'Отправте номер автобуса в чат от 1-50',
    "kontroler_trolleubus_msg": 'Отправте номер троллейбуса в чат от 1-9',
    "settings_sort_msg": "Настройка сортировки постов.",
    "settings_sort_inside_msg": "Теперь сообщения сортируются по {msg_pref}",
    "settings_display_msg": 'Настройка отображения постов.',
    "settings_display_inside_msg": 'Теперь информация отображается {display}',
    "settings_time_msg": 'Настройка времени получения постов.',
    "settings_time_inside_msg": 'Время отборки постов изменено на {final_time}'
}

MESSAGE_KEYBOARD = {
    'back_keyb': 'Назад',
    'menu_keyb': 'Меню',
    'start_keyb_kontroler': 'Контроллеры',
    'start_keyb_settings': 'Настройки',
    'kontroler_keyb_clear_stop': 'Чистые остановки',
    'kontroler_keyb_dirty_stop': 'Грязные остановки',
    'kontroler_keyb_bus': 'Автобусы',
    'kontroler_keyb_trolleybus': 'Тролейбусы',
    'settings_keyb_time': 'Время',
    'settings_keyb_time_inside_1': '30 мин',
    'settings_keyb_time_inside_2': '1 час',
    'settings_keyb_time_inside_3': '1 час 30 мин',
    'settings_keyb_time_inside_4': '2 часа',
    'settings_keyb_time_inside_5': '2 часа 30 мин',
    'settings_keyb_time_inside_6': '3 часа',
    'settings_keyb_display': 'Отображение',
    'settings_keyb_display_inside_1': 'Фото',
    'settings_keyb_display_inside_2': 'Текст',
    'settings_keyb_sort': 'Сортировка',
    'settings_keyb_sort_inside_1': 'Время',
    'settings_keyb_sort_inside_2': 'Сообщения',
}

bus_number = ['1', '1А', '2', '2А', '3', '4', '5', '6', '7', '8', '9', '10', '11', '11А', '12', '12А', '13', '13А', '14', '15', '15А', '15Б', '16', '17', '18', '19', '20', '21', '21А', '21Б', '22', '23', '23А', '23Б', '24', '24А', '25', '26', '27', '27А', '28', '29', '30', '30А', '31', '32', '33', '34', '35', '36', '37', '37А', '38', '39', '39А', '39Б', '40', '41', '42', '43', '44', '44А', '45', '46', '47', '50']
trolleybus_number = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
