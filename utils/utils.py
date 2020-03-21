from configuration.message import MESSAGE_KEYBOARD


def converting_time(sec_time: int):
    """ Добавления правильного окончания для времени """
    hours = sec_time // 3600
    minutes = None
    if sec_time % 3600 == 0.0:
        pass
    else:
        minutes = int((sec_time - hours * 3600) / 60)

    if hours == 1:
        hours_prefix = "час"
    else:
        hours_prefix = "часа"

    min_prefix = "минут"
    if hours == 0:
        return f'{minutes} {min_prefix}'
    elif minutes:
        return f'{hours} {hours_prefix} {minutes} {min_prefix}'
    else:
        return f'{hours} {hours_prefix}'


def deconverting_time(time: str):
    """ Декодирование окончания в секунды """
    _str = time.split()
    sec = 0
    if len(_str) == 2:
        if _str[1] == "час":
            sec += 3600
        elif _str[1] == "часа":
            if len(_str) == 2:
                sec += int(_str[0]) * 3600
        elif _str[1] == "мин":
            sec = 1800
    else:
        sec += (int(_str[0]) * 3600) + 1800
    return sec


def text_display(data: list):
    """ Представление словаря в тексте """
    text = '\n'.join([f'{stop[0]}, {stop[1][0]}, {stop[1][1]}' for stop in data])
    if text:
        return text
    else:
        return 'Остутствуют сообщения людей.'


def get_data_from_list(data_list: list) -> list:
    text_city = []
    for _ in data_list:
        for text_keyb in _:
            if text_keyb == MESSAGE_KEYBOARD['back_keyb'] or text_keyb == MESSAGE_KEYBOARD['menu_keyb']:
                continue
            text_city.append(text_keyb)
    return text_city
