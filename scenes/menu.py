from aiogram.types import Message
from scene_loader import BaseScene
from configuration.message import MESSAGE, MESSAGE_KEYBOARD
from utils.keyboard import create_keyboard
from configuration.keyboard import kontroler_keyboard, settings_keyboard, menu_keyboard


class Scene(BaseScene):
    async def message_handler(self, message: Message):
        msg_text = message.text.lower()
        if msg_text == MESSAGE_KEYBOARD['start_keyb_kontroler'].lower():
            self.user_data[0].scens = "kontroler"
            await self.manager.update(self.user_data[0])
            keyb = create_keyboard(kontroler_keyboard)
            await message.answer(MESSAGE["kontroler_msg"], reply_markup=keyb)
        elif msg_text == MESSAGE_KEYBOARD['start_keyb_settings'].lower():
            keyb = create_keyboard(settings_keyboard)
            self.user_data[0].scens = "settings"
            await self.manager.update(self.user_data[0])
            await message.answer(MESSAGE["settings_msg"], reply_markup=keyb)
        elif msg_text == MESSAGE_KEYBOARD['start_keyb_info'].lower():
            keyb = create_keyboard(menu_keyboard)
            await message.answer(MESSAGE["info_msg"], reply_markup=keyb)
