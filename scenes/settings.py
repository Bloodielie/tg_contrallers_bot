from scene_loader import BaseScene
from aiogram.types import Message
from config import MESSAGE_KEYBOARD, MESSAGE
from utils.keyboard import create_keyboard
from configuration.keyboard import settings_sort_keyboard, settings_display_keyboard, settings_time_keyboard, menu_keyboard, \
    settings_city_keyboard


class Scene(BaseScene):
    async def message_handler(self, message: Message):
        msg_text = message.text.lower()
        if msg_text == MESSAGE_KEYBOARD['settings_keyb_sort'].lower():
            self.user_data[0].scens = 'settings_sort'
            await self.manager.update(self.user_data[0])
            keyb = create_keyboard(settings_sort_keyboard)
            await message.answer(MESSAGE['settings_sort_msg'], reply_markup=keyb)
        elif msg_text == MESSAGE_KEYBOARD['settings_keyb_display'].lower():
            self.user_data[0].scens = 'settings_display'
            await self.manager.update(self.user_data[0])
            keyb = create_keyboard(settings_display_keyboard)
            await message.answer(MESSAGE['settings_display_msg'], reply_markup=keyb)
        elif msg_text == MESSAGE_KEYBOARD['settings_keyb_time'].lower():
            self.user_data[0].scens = 'settings_time'
            await self.manager.update(self.user_data[0])
            keyb = create_keyboard(settings_time_keyboard)
            await message.answer(MESSAGE['settings_time_msg'], reply_markup=keyb)
        elif msg_text == MESSAGE_KEYBOARD['settings_city'].lower():
            self.user_data[0].scens = 'settings_city'
            await self.manager.update(self.user_data[0])
            keyb = create_keyboard(settings_city_keyboard)
            await message.answer(MESSAGE['settings_time_msg'], reply_markup=keyb)
        elif msg_text == MESSAGE_KEYBOARD['back_keyb'].lower():
            self.user_data[0].scens = 'menu'
            await self.manager.update(self.user_data[0])
            keyb = create_keyboard(menu_keyboard)
            await message.answer(MESSAGE['menu_msg'], reply_markup=keyb)
