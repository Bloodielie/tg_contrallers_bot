from scene_loader import BaseScene
from aiogram.types import Message, InputFile
from utils.utils import text_display
from utils.pil import img_busstop
from config import DEFAULT_TABLE_BUS, SAVE_DEFAULT_TABLE_BUS, FONT_PNG, MESSAGE_KEYBOARD


class Scene(BaseScene):
    async def message_handler(self, message: Message):
        text = message.text
        _data = await self.manager.get(self.model, user_id=message.from_user.id)
        temporary_data: dict = await self.getter.get_data_bus(city=_data.city, type_stop='dirty', transport_number=text, time=_data.time, sort=_data.sort)
        if text == MESSAGE_KEYBOARD['back_keyb']:
            _data.scens = 'kontroler'
            await self.manager.update(_data)
            await self.bot.send_message(message.from_user.id, self.lang['kontroler_msg'], reply_markup=self.keyboard.kontroler_keyboard())
        elif text == self.lang['menu']:
            await self.bot.send_message(message.from_user.id, '', reply_markup=self.keyboard.start_keyboard())
        elif not temporary_data:
            await self.bot.send_message(message.from_user.id, self.lang['not_people_msg'], reply_markup=self.keyboard.kontroler_bus())
        elif temporary_data[0][0] == 'number_bus_not_found':
            await self.bot.send_message(message.from_user.id, self.lang['not_bus'], reply_markup=self.keyboard.kontroler_bus())
        elif temporary_data:
            if _data.display == 'Фото':
                img_busstop(name_png=SAVE_DEFAULT_TABLE_BUS, _dict=temporary_data, cordinates_x=(60, 650, 1250), cordinate_y=45, y_step=92,
                            color=(34, 34, 34), font=FONT_PNG, name_png_first=DEFAULT_TABLE_BUS)
                await self.bot.send_photo(message.from_user.id, InputFile('png/tablebus.gif'), reply_markup=self.keyboard.kontroler_bus())
            else:
                texts = text_display(temporary_data)
                await self.bot.send_message(message.from_user.id, texts, reply_markup=self.keyboard.kontroler_bus())
