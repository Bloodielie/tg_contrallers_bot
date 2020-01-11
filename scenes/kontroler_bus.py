from scene_loader import BaseScene
from aiogram.types import Message, InputFile
from utils.validation import temporary_list, BusStopCheck, check_bus
from utils.utils import text_display
from utils.pil import img_busstop
from config import JSON_BUS_STOP, DEFAULT_TABLE_BUS, SAVE_DEFAULT_TABLE_BUS, FONT_PNG, bus_number, MESSAGE_KEYBOARD


class Scene(BaseScene):
    async def message_handler(self, message: Message):
        text = message.text
        bus_check = BusStopCheck()
        _data = await self.manager.get(self.model, user_id=message.from_user.id)
        if text in bus_number:
            temporary_data = temporary_list(time_=_data.time, path_file=JSON_BUS_STOP)
            data = bus_check.sort_busstop(check_bus(type_bus='bus', data=temporary_data, bus_number=text), _sort=_data.sort)
            if _data.display == 'Фото':
                img_busstop(name_png=SAVE_DEFAULT_TABLE_BUS, _dict=data, cordinates_x=(60, 650, 1250), cordinate_y=45, y_step=92,
                            color=(34, 34, 34), font=FONT_PNG, name_png_first=DEFAULT_TABLE_BUS)
                await self.bot.send_photo(message.from_user.id, InputFile('png/tablebus.gif'), reply_markup=self.keyboard.kontroler_bus())
            else:
                texts = text_display(data)
                await self.bot.send_message(message.from_user.id, texts, reply_markup=self.keyboard.kontroler_bus())
        elif text == MESSAGE_KEYBOARD['back_keyb']:
            _data.scens = 'kontroler'
            await self.manager.update(_data)
            await self.bot.send_message(message.from_user.id, self.lang['kontroler_msg'], reply_markup=self.keyboard.kontroler_keyboard())
