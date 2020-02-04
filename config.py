from utils.json import JsonUtils

token = ''
login = ''
password = ''

db_name = 'controller_base'
user = 'postgres'
host = 'localhost'
password_db =

SAVE_DEFAULT_TABLE = 'png/table.gif'
SAVE_DEFAULT_TABLE_CLEAR = 'png/tableclear.gif'
DEFAULT_TABLE = 'png/таблица.png'

DEFAULT_TABLE_BUS = 'png/таблицадляавтобуса.png'
SAVE_DEFAULT_TABLE_BUS = 'png/tablebus.gif'
SAVE_DEFAULT_TABLE_TROLLEYBUSES = 'png/tabletrolleybuses.gif'

JSON_BUS = 'json/busstop.json'
JSON_TROLLEYBUSES = 'json/trolleybusesstop.json'

FONT_PNG = 'font/impact.ttf'

stop_bus = JsonUtils('json/stopbus.json').get_json()

MESSAGE_KEYBOARD = {
    'back_keyb': 'Назад',
    'menu_keyb': 'Меню',
    'start_keyb_kontroler': 'Контроллеры',
    'start_keyb_settings': 'Настройки',
    'start_keyb_info': 'Информация',
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
    'settings_city': 'Город',
    'settings_city_1': 'Брест',
    'settings_city_2': 'Гомель',
    'settings_city_3': 'Гродно'
}

MESSAGE = {
    "start_msg": 'Привет! Я Контролер бот для г.Брест.\n Использую клавиатуру ниже чтобы использовать меня.',
    "kontroler_msg": 'Контроллеры.',
    "settings_msg": 'Доступные настройки.',
    "menu_msg": 'Главное меню.',
    "kontroler_bus_msg": 'Отправте номер автобуса в чат',
    "kontroler_trolleubus_msg": 'Отправте номер троллейбуса в чат',
    "settings_sort_msg": "Настройка сортировки постов.",
    "settings_sort_inside_msg": "Теперь сообщения сортируются по {msg_pref}",
    "settings_display_msg": 'Настройка отображения постов.',
    "settings_display_inside_msg": 'Теперь информация отображается {display}',
    "settings_time_msg": 'Настройка времени получения постов.',
    "settings_time_inside_msg": 'Время отборки постов изменено на {final_time}',
    "settings_city_start": 'Выберите город.',
    "settings_city": 'Теперь ваш город {city_name}',
    'info_msg': 'Бот для отслеживать контроллеров в г.Бресте.\nПочти точно такой же бот в VK:\nhttps://vk.com/anti_controllers',
    'not_people_msg': 'Отсутствуют сообщения людей!',
    'not_bus': 'Такого автобуса не существует!',
    'not_trolleibys': 'Такого троллейбуса не существует!',
    'menu': 'Меню'
}

alias_city = {MESSAGE_KEYBOARD['settings_city_1']: 'brest',
              MESSAGE_KEYBOARD['settings_city_2']: 'gomel',
              MESSAGE_KEYBOARD['settings_city_3']: 'grodno'}
