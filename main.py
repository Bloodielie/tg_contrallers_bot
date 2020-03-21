from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher
from scene_loader import Loader
from configuration.config import Config
from configuration.message import MESSAGE_KEYBOARD, MESSAGE
from database import database, User
import peewee_async
from utils.api_getter import ApiGetter
import logging
from utils.keyboard import create_keyboard
from configuration.keyboard import menu_keyboard, start_keyboard

#logging.basicConfig(filename="error.log", format='\n%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.ERROR)
#logger = logging.getLogger(__name__)

load = Loader()
manager = peewee_async.Manager(database)
getter_data = ApiGetter('http://127.0.0.1:8000')
config = Config()

bot = Bot(token=config.get_data('app', 'TELEGRAM_TOKEN'))
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    id = message.from_user.id
    user = (await manager.create_or_get(User, user_id=id))[0]
    keyb = create_keyboard(start_keyboard)
    if not user.scens == 'start':
        user.scens = 'start'
        await manager.update(user)
    await message.answer(MESSAGE['start_msg'], reply_markup=keyb)


@dp.message_handler()
async def message(msg: types.Message):
    data = await manager.create_or_get(User, user_id=msg.from_user.id)
    if msg.text == MESSAGE_KEYBOARD['menu_keyb']:
        data[0].scens = "menu"
        await manager.update(data[0])
        keyb = create_keyboard(menu_keyboard)
        await msg.answer(MESSAGE["menu_msg"], reply_markup=keyb)

    await load.init_scene(data[0].scens, bot, manager, data, getter_data).message_handler(msg)


if __name__ == '__main__':
    executor.start_polling(dp)
