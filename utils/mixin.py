from aiogram import types
from .pil import img_busstop
from .utils import text_display
from utils.keyboard import create_keyboard
from configuration.keyboard import kontroler_keyboard
from models import User
from aiogram.types import Message


async def mixin_create_kontroler(user_data: User, temporary_data: list, message: Message, DEFAULT_TABLE: str, SAVE_DEFAULT_TABLE: str):
    keyb = create_keyboard(kontroler_keyboard)
    if user_data.display.lower() == 'фото':
        img_busstop(name_png=SAVE_DEFAULT_TABLE, _data=temporary_data, name_png_first=DEFAULT_TABLE)
        await message.answer_photo(types.InputFile(SAVE_DEFAULT_TABLE), reply_markup=keyb)
    else:
        text: str = text_display(temporary_data)
        await message.answer(text, reply_markup=keyb)
