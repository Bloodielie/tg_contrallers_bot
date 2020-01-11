from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from config import MESSAGE_KEYBOARD


class Keyboard:
    def start_keyboard(self):
        keyboard = ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
        keyboard.add(KeyboardButton(MESSAGE_KEYBOARD['start_keyb_kontroler']))
        keyboard.add(KeyboardButton(MESSAGE_KEYBOARD['start_keyb_settings']))
        return keyboard

    def kontroler_keyboard(self):
        keyboard = ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
        keyboard.row(KeyboardButton(MESSAGE_KEYBOARD['kontroler_keyb_clear_stop']))
        keyboard.insert(KeyboardButton(MESSAGE_KEYBOARD['kontroler_keyb_dirty_stop']))
        keyboard.row(KeyboardButton(MESSAGE_KEYBOARD['kontroler_keyb_bus']))
        keyboard.insert(KeyboardButton(MESSAGE_KEYBOARD['kontroler_keyb_trolleybus']))
        keyboard.add(KeyboardButton(MESSAGE_KEYBOARD['back_keyb']))
        keyboard.add(KeyboardButton(MESSAGE_KEYBOARD['menu_keyb']))
        return keyboard

    def kontroler_bus(self):
        keyboard = ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
        keyboard.add(KeyboardButton(MESSAGE_KEYBOARD['back_keyb']))
        keyboard.add(KeyboardButton(MESSAGE_KEYBOARD['menu_keyb']))
        return keyboard

    def settings_keyboard(self):
        keyboard = ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
        keyboard.add(KeyboardButton(MESSAGE_KEYBOARD['settings_keyb_time']))
        keyboard.insert(KeyboardButton(MESSAGE_KEYBOARD['settings_keyb_display']))
        keyboard.insert(KeyboardButton(MESSAGE_KEYBOARD['settings_keyb_sort']))
        keyboard.add(KeyboardButton(MESSAGE_KEYBOARD['back_keyb']))
        keyboard.add(KeyboardButton(MESSAGE_KEYBOARD['menu_keyb']))
        return keyboard

    def settings_time_keyboard(self):
        keyboard = ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
        keyboard.add(KeyboardButton(MESSAGE_KEYBOARD['settings_keyb_time_inside_1']))
        keyboard.insert(KeyboardButton(MESSAGE_KEYBOARD['settings_keyb_time_inside_2']))
        keyboard.add(KeyboardButton(MESSAGE_KEYBOARD['settings_keyb_time_inside_3']))
        keyboard.insert(KeyboardButton(MESSAGE_KEYBOARD['settings_keyb_time_inside_4']))
        keyboard.add(KeyboardButton(MESSAGE_KEYBOARD['settings_keyb_time_inside_5']))
        keyboard.insert(KeyboardButton(MESSAGE_KEYBOARD['settings_keyb_time_inside_6']))
        keyboard.add(KeyboardButton(MESSAGE_KEYBOARD['back_keyb']))
        keyboard.add(KeyboardButton(MESSAGE_KEYBOARD['menu_keyb']))
        return keyboard

    def settings_sort_keyboard(self):
        keyboard = ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
        keyboard.add(KeyboardButton(MESSAGE_KEYBOARD['settings_keyb_sort_inside_1']))
        keyboard.insert(KeyboardButton(MESSAGE_KEYBOARD['settings_keyb_sort_inside_2']))
        keyboard.add(KeyboardButton(MESSAGE_KEYBOARD['back_keyb']))
        keyboard.add(KeyboardButton(MESSAGE_KEYBOARD['menu_keyb']))
        return keyboard

    def settings_display_keyboard(self):
        keyboard = ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
        keyboard.add(KeyboardButton(MESSAGE_KEYBOARD['settings_keyb_display_inside_1']))
        keyboard.insert(KeyboardButton(MESSAGE_KEYBOARD['settings_keyb_display_inside_2']))
        keyboard.add(KeyboardButton(MESSAGE_KEYBOARD['back_keyb']))
        keyboard.add(KeyboardButton(MESSAGE_KEYBOARD['menu_keyb']))
        return keyboard
