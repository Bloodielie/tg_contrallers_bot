from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def create_keyboard(data: list):
    keyboard = ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
    for list_data in data:
        row = []
        for value in list_data:
            row.append(KeyboardButton(str(value)))
        keyboard.row(*row)
    return keyboard

