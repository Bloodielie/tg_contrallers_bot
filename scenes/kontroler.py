from scene_loader import BaseScene
from aiogram.types import Message
from aiogram import types
from config import SAVE_DEFAULT_TABLE, DEFAULT_TABLE, FONT_PNG, MESSAGE_KEYBOARD
from utils.pil import img_busstop
from utils.utils import text_display
from utils.mixin import mixin_create_kontroler


class Scene(BaseScene):
    async def message_handler(self, message: Message):
        data = await self.manager.get(self.model, user_id=message.from_user.id)
        if message.text == MESSAGE_KEYBOARD['kontroler_keyb_clear_stop']:
            temporary_data = await self.getter.get_data_bus(type='clean', time=data.time, sort=data.sort)
            await mixin_create_kontroler(self.bot, data, temporary_data, self.keyboard, message, FONT_PNG, DEFAULT_TABLE, SAVE_DEFAULT_TABLE)
            #if data.display == 'Фото':
            #    img_busstop(name_png=SAVE_DEFAULT_TABLE, _dict=temporary_data, cordinates_x=(60, 650, 1250), cordinate_y=45, y_step=92,
            #                color=(34, 34, 34), font=FONT_PNG, name_png_first=DEFAULT_TABLE)
            #    await self.bot.send_photo(message.from_user.id, types.InputFile('png/table.gif'), reply_markup=self.keyboard.kontroler_keyboard())
            #else:
            #    text = text_display(temporary_data)
            #    await self.bot.send_message(message.from_user.id, text, reply_markup=self.keyboard.kontroler_keyboard())
        elif message.text == MESSAGE_KEYBOARD['kontroler_keyb_dirty_stop']:
            temporary_data = await self.getter.get_data_bus(type='dirty', time=data.time, sort=data.sort)
            await mixin_create_kontroler(self.bot, data, temporary_data, self.keyboard, message, FONT_PNG, DEFAULT_TABLE, SAVE_DEFAULT_TABLE)
            #if data.display == 'Фото':
            #    img_busstop(name_png=SAVE_DEFAULT_TABLE, _dict=temporary_data, cordinates_x=(60, 650, 1250), cordinate_y=45, y_step=92,
            #                color=(34, 34, 34), font=FONT_PNG, name_png_first=DEFAULT_TABLE)
            #    await self.bot.send_photo(message.from_user.id, types.InputFile('png/table.gif'), reply_markup=self.keyboard.kontroler_keyboard())
            #else:
            #    text = text_display(temporary_data)
            #    await self.bot.send_message(message.from_user.id, text, reply_markup=self.keyboard.kontroler_keyboard())
        elif message.text == MESSAGE_KEYBOARD['kontroler_keyb_bus']:
            data.scens = 'kontroler_bus'
            await self.manager.update(data)
            await self.bot.send_message(message.from_user.id, self.lang['kontroler_bus_msg'], reply_markup=self.keyboard.kontroler_bus())
        elif message.text == MESSAGE_KEYBOARD['kontroler_keyb_trolleybus']:
            data.scens = 'kontroler_trolleybus'
            await self.manager.update(data)
            await self.bot.send_message(message.from_user.id, self.lang['kontroler_trolleubus_msg'], reply_markup=self.keyboard.kontroler_bus())
        elif message.text == MESSAGE_KEYBOARD['back_keyb']:
            data.scens = 'kontroler'
            await self.manager.update(data)
            await self.bot.send_message(message.from_user.id, self.lang['menu_msg'], reply_markup=self.keyboard.start_keyboard())
