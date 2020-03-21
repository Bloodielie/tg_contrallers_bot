from aiogram.types import Message
from scene_loader import BaseScene
from configuration.message import MESSAGE, MESSAGE_KEYBOARD
from utils.keyboard import create_keyboard
from configuration.keyboard import menu_keyboard, start_keyboard


class Scene(BaseScene):
    async def message_handler(self, message: Message):
        msg_text = message.text.lower()
        keyb = create_keyboard(menu_keyboard)
        message_answer = MESSAGE["menu_msg"]
        self.user_data[0].scens = "menu"
        if msg_text == MESSAGE_KEYBOARD['settings_city_1'].lower():
            self.user_data[0].city = "brest"
            await self.manager.update(self.user_data[0])
            await message.answer(message_answer, reply_markup=keyb)
        elif msg_text == MESSAGE_KEYBOARD['settings_city_2'].lower():
            self.user_data[0].city = "gomel"
            await self.manager.update(self.user_data[0])
            await message.answer(message_answer, reply_markup=keyb)
        elif msg_text == MESSAGE_KEYBOARD['settings_city_3'].lower():
            self.user_data[0].city = "grodno"
            await self.manager.update(self.user_data[0])
            await message.answer(message_answer, reply_markup=keyb)
        else:
            keyb = create_keyboard(start_keyboard)
            await message.answer(MESSAGE['city_available'], reply_markup=keyb)
