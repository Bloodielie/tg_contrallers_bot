from scene_loader import BaseScene
from aiogram.types import Message
from config import MESSAGE_KEYBOARD


class Scene(BaseScene):
    async def message_handler(self, message: Message):
        text = message.text
        data = await self.manager.get(self.model, user_id=message.from_user.id)
        if text == MESSAGE_KEYBOARD['settings_keyb_display_inside_1']:
            display_pref = 'картинками'
            data.display = text
            await self.manager.update(data)
            await self.bot.send_message(message.from_user.id, self.lang['settings_display_inside_msg'].format(display=display_pref), reply_markup=self.keyboard.start_keyboard())
        elif text == MESSAGE_KEYBOARD['settings_keyb_display_inside_2']:
            display_ = 'Сообщения'
            display_pref = 'текстом'
            data.display = display_
            await self.manager.update(data)
            await self.bot.send_message(message.from_user.id, self.lang['settings_display_inside_msg'].format(display=display_pref), reply_markup=self.keyboard.start_keyboard())
        elif text == MESSAGE_KEYBOARD['back_keyb']:
            data.scens = 'settings'
            await self.manager.update(data)
            await self.bot.send_message(message.from_user.id, self.lang['settings_msg'], reply_markup=self.keyboard.settings_keyboard())
