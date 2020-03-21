from aiogram import types
from .pil import img_busstop
from .utils import text_display


async def mixin_create_kontroler(bot, data, temporary_data, keyboard, message, FONT_PNG, DEFAULT_TABLE, SAVE_DEFAULT_TABLE):
    if data.display == 'Фото':
        img_busstop(name_png=SAVE_DEFAULT_TABLE, _dict=temporary_data, cordinates_x=(60, 650, 1250), cordinate_y=45, y_step=92,
                    color=(34, 34, 34), font=FONT_PNG, name_png_first=DEFAULT_TABLE)
        await bot.send_photo(message.from_user.id, types.InputFile(SAVE_DEFAULT_TABLE), reply_markup=keyboard.kontroler_keyboard())
    else:
        text = text_display(temporary_data)
        await bot.send_message(message.from_user.id, text, reply_markup=keyboard.kontroler_keyboard())
