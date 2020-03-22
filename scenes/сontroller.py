from scene_loader import BaseScene
from aiogram.types import Message
from configuration.config import Config
from utils.mixin import mixin_create_kontroler
from configuration.message import MESSAGE, MESSAGE_KEYBOARD
from utils.keyboard import create_keyboard
from configuration.keyboard import kontroler_bus


class Scene(BaseScene):
    async def message_handler(self, message: Message):
        config = Config()
        SAVE_DEFAULT_TABLE = config.get_data('pillow', 'SAVE_DEFAULT_TABLE')
        DEFAULT_TABLE = config.get_data('pillow', 'DEFAULT_TABLE')
        data = self.user_data[0]
        if message.text == MESSAGE_KEYBOARD['kontroler_keyb_clear_stop']:
            temporary_data = await self.getter.get_date(f'{data.city}/clean', type_return='list', time=data.time,
                                                        sort=data.sort.capitalize())
            await mixin_create_kontroler(data, temporary_data, message, DEFAULT_TABLE, SAVE_DEFAULT_TABLE)
        elif message.text == MESSAGE_KEYBOARD['kontroler_keyb_dirty_stop']:
            temporary_data = await self.getter.get_date(f'{data.city}/dirty', type_return='list', time=data.time,
                                                        sort=data.sort.capitalize())
            await mixin_create_kontroler(data, temporary_data, message, DEFAULT_TABLE, SAVE_DEFAULT_TABLE)
        elif message.text == MESSAGE_KEYBOARD['kontroler_keyb_bus']:
            data.scens = 'controller_bus'
            await self.manager.update(data)
            keyb = create_keyboard(kontroler_bus)
            await message.answer(MESSAGE['kontroler_bus_msg'], reply_markup=keyb)
        elif message.text == MESSAGE_KEYBOARD['kontroler_keyb_trolleybus']:
            data.scens = 'controller_trolleybus'
            await self.manager.update(data)
            keyb = create_keyboard(kontroler_bus)
            await message.answer(MESSAGE['kontroler_trolleubus_msg'], reply_markup=keyb)
