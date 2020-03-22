MESSAGE_KEYBOARD = {
    'back_keyb': 'Назад',
    'menu_keyb': 'Меню',
    'start_keyb_kontroler': 'Контроллеры',
    'start_keyb_settings': 'Настройки',
    'start_keyb_info': 'Информация',
    'kontroler_keyb_clear_stop': 'Чистые остановки',
    'kontroler_keyb_dirty_stop': 'Грязные остановки',
    'kontroler_keyb_bus': 'Автобусы',
    'kontroler_keyb_trolleybus': 'Троллейбусы',
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
    "start_msg": 'Привет! Я Контролер бот для г Брест, Гомель, Гродно.\n Выберите ваш город.',
    "kontroler_msg": 'Контроллеры.',
    "settings_msg": 'Доступные настройки.',
    "menu_msg": 'Главное меню.',
    "kontroler_bus_msg": 'Отправьте номер автобуса в чат',
    "kontroler_trolleubus_msg": 'Отправьте номер троллейбуса в чат',
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
    'menu': 'Меню',
    'city_available': 'Доступные города: Брест, Гомель, Гродно.',
    'spam_msg': 'Хватит спамить!'
}

alias_city = {MESSAGE_KEYBOARD['settings_city_1']: 'brest',
              MESSAGE_KEYBOARD['settings_city_2']: 'gomel',
              MESSAGE_KEYBOARD['settings_city_3']: 'grodno'}

