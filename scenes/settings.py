from scene_loader import BaseScene
from aiogram.types import Message
from config import MESSAGE_KEYBOARD

times_tabl = ['30 мин', '1 час', '1 час 30 мин', '2 часа', '2 часа 30 мин', '3 часа']


class Scene(BaseScene):
    async def message_handler(self, message: Message):
        data = await self.manager.get(self.model, user_id=message.from_user.id)
        if message.text == MESSAGE_KEYBOARD['settings_keyb_sort']:
            data.scens = 'settings_sort'
            await self.manager.update(data)
            await self.bot.send_message(message.from_user.id, self.lang['settings_sort_msg'], reply_markup=self.keyboard.settings_sort_keyboard())
        elif message.text == MESSAGE_KEYBOARD['settings_keyb_display']:
            data.scens = 'settings_display'
            await self.manager.update(data)
            await self.bot.send_message(message.from_user.id, self.lang['settings_display_msg'], reply_markup=self.keyboard.settings_display_keyboard())
        elif message.text == MESSAGE_KEYBOARD['settings_keyb_time']:
            data.scens = 'settings_time'
            await self.manager.update(data)
            await self.bot.send_message(message.from_user.id, self.lang['settings_time_msg'], reply_markup=self.keyboard.settings_time_keyboard())
        elif message.text == MESSAGE_KEYBOARD['back_keyb']:
            await self.bot.send_message(message.from_user.id, self.lang['menu_msg'], reply_markup=self.keyboard.start_keyboard())
