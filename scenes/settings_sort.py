from scene_loader import BaseScene
from aiogram.types import Message
from config import MESSAGE_KEYBOARD


class Scene(BaseScene):
    async def message_handler(self, message: Message):
        text = message.text
        data = await self.manager.get(self.model, user_id=message.from_user.id)
        if text == MESSAGE_KEYBOARD['settings_keyb_sort_inside_1']:
            str_pref = 'времени'
            data.sort = text
            await self.manager.update(data)
            await self.bot.send_message(message.from_user.id, self.lang["settings_sort_inside_msg"].format(msg_pref=str_pref), reply_markup=self.keyboard.start_keyboard())
        elif text == MESSAGE_KEYBOARD['settings_keyb_sort_inside_2']:
            str_pref = 'сообщениям'
            data.sort = text
            await self.manager.update(data)
            await self.bot.send_message(message.from_user.id, self.lang["settings_sort_inside_msg"].format(msg_pref=str_pref), reply_markup=self.keyboard.start_keyboard())
        elif text == MESSAGE_KEYBOARD['back_keyb']:
            data.scens = 'settings'
            await self.manager.update(data)
            await self.bot.send_message(message.from_user.id, self.lang["settings_msg"], reply_markup=self.keyboard.settings_keyboard())
