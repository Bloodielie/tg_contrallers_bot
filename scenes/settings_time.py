from scene_loader import BaseScene
from aiogram.types import Message
from utils.utils import deconverting_time
from configuration.message import MESSAGE_KEYBOARD, MESSAGE
from utils.keyboard import create_keyboard
from configuration.keyboard import menu_keyboard, settings_keyboard, settings_time_keyboard
from utils.utils import get_data_from_list


class Scene(BaseScene):
    async def message_handler(self, message: Message):
        text = message.text
        text_time = get_data_from_list(settings_time_keyboard)
        if text in text_time:
            time = deconverting_time(text)
            self.user_data[0].time = time
            self.user_data[0].scens = 'menu'
            await self.manager.update(self.user_data[0])
            keyb = create_keyboard(menu_keyboard)
            await message.answer(MESSAGE['settings_time_inside_msg'].format(final_time=message.text), reply_markup=keyb)
        elif text == MESSAGE_KEYBOARD['back_keyb']:
            self.user_data[0].scens = 'settings'
            await self.manager.update(self.user_data[0])
            keyb = create_keyboard(settings_keyboard)
            await message.answer(MESSAGE["settings_msg"], reply_markup=keyb)
