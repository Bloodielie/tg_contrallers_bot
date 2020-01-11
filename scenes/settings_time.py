from scene_loader import BaseScene
from aiogram.types import Message
from utils.utils import deconverting_time
from config import MESSAGE_KEYBOARD

times_tabl = [MESSAGE_KEYBOARD['settings_keyb_time_inside_1'], MESSAGE_KEYBOARD['settings_keyb_time_inside_2'], MESSAGE_KEYBOARD['settings_keyb_time_inside_3'], MESSAGE_KEYBOARD['settings_keyb_time_inside_4'], MESSAGE_KEYBOARD['settings_keyb_time_inside_5'], MESSAGE_KEYBOARD['settings_keyb_time_inside_6']]


class Scene(BaseScene):
    async def message_handler(self, message: Message):
        text = message.text
        data = await self.manager.get(self.model, user_id=message.from_user.id)
        if text in times_tabl:
            time = deconverting_time(text)
            data.time = time
            await self.manager.update(data)
            await self.bot.send_message(message.from_user.id, self.lang['settings_time_inside_msg'].format(final_time=message.text), reply_markup=self.keyboard.start_keyboard())
        elif text == MESSAGE_KEYBOARD['back_keyb']:
            data.scens = 'settings'
            await self.manager.update(data)
            await self.bot.send_message(message.from_user.id, self.lang["settings_msg"], reply_markup=self.keyboard.settings_keyboard())
