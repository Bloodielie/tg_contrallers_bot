from scene_loader import BaseScene
from aiogram.types import Message, InputFile
from utils.utils import text_display
from utils.pil import img_busstop
from configuration.message import MESSAGE_KEYBOARD, MESSAGE
from configuration.config import Config
from utils.keyboard import create_keyboard
from configuration.keyboard import kontroler_bus, kontroler_keyboard


class Scene(BaseScene):
    async def message_handler(self, message: Message):
        config = Config()
        DEFAULT_TABLE_BUS = config.get_data('pillow', 'DEFAULT_TABLE_BUS')
        SAVE_DEFAULT_TABLE_TROLLEYBUSES = config.get_data('pillow', 'SAVE_DEFAULT_TABLE_TROLLEYBUSES')
        text = message.text
        data = self.user_data[0]
        temporary_data = await self.getter.get_date(f'{data.city}/dirty/trolleybus/{text}', type_return='list', time=data.time,
                                                    sort=data.sort.capitalize())
        if text == MESSAGE_KEYBOARD['back_keyb']:
            data.scens = 'kontroler'
            await self.manager.update(data)
            keyb = create_keyboard(kontroler_keyboard)
            await message.answer(MESSAGE['kontroler_msg'], reply_markup=keyb)
        elif not temporary_data:
            keyb = create_keyboard(kontroler_bus)
            await message.answer(MESSAGE['not_people_msg'], reply_markup=keyb)
        elif temporary_data[0][0] == 'number_bus_not_found':
            keyb = create_keyboard(kontroler_bus)
            await message.answer(MESSAGE['not_trolleibys'], reply_markup=keyb)
        elif temporary_data:
            keyb = create_keyboard(kontroler_bus)
            if data.display.lower() == 'фото':
                img_busstop(name_png=SAVE_DEFAULT_TABLE_TROLLEYBUSES, _data=temporary_data, name_png_first=DEFAULT_TABLE_BUS)
                await message.answer_photo(InputFile('png/tabletrolleybuses.gif'), reply_markup=keyb)
            else:
                texts = text_display(temporary_data)
                await message.answer(texts, reply_markup=keyb)
