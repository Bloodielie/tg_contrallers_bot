from scene_loader import BaseScene
from aiogram.types import Message
from config import MESSAGE_KEYBOARD, MESSAGE
from utils.keyboard import create_keyboard
from configuration.keyboard import menu_keyboard, settings_keyboard


class Scene(BaseScene):
    async def message_handler(self, message: Message):
        text: str = message.text.lower()
        keyb = create_keyboard(menu_keyboard)
        self.user_data[0].scens = 'menu'
        if text == MESSAGE_KEYBOARD['settings_keyb_sort_inside_1'].lower():
            self.user_data[0].sort = text
            await self.manager.update(self.user_data[0])
            await message.answer(MESSAGE["settings_sort_inside_msg"].format(msg_pref='времени'), reply_markup=keyb)
        elif text == MESSAGE_KEYBOARD['settings_keyb_sort_inside_2'].lower():
            self.user_data[0].sort = text
            await self.manager.update(self.user_data[0])
            await message.answer(MESSAGE["settings_sort_inside_msg"].format(msg_pref='сообщениям'), reply_markup=keyb)
        elif text == MESSAGE_KEYBOARD['back_keyb'].lower():
            self.user_data[0].scens = 'settings'
            await self.manager.update(self.user_data[0])
            keyb = create_keyboard(settings_keyboard)
            await message.answer(MESSAGE["settings_msg"], reply_markup=keyb)
