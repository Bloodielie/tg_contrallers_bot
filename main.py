from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher
from scene_loader import Loader
from configuration.config import Config
from configuration.message import MESSAGE_KEYBOARD, MESSAGE
from models import database, UserSettings
import peewee_async
from utils.api_getter import ApiGetter
import logging
from utils.keyboard import create_keyboard
from configuration.keyboard import menu_keyboard, start_keyboard
from utils.spam_filter import SpamFilter

logging.basicConfig(filename="error.log", format='\n%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.ERROR)
logger = logging.getLogger(__name__)


config = Config()
load = Loader()
manager = peewee_async.Manager(database)
getter_data = ApiGetter(config.get_data('app', 'API_URL'))

bot = Bot(token=config.get_data('app', 'TELEGRAM_TOKEN'))
dp = Dispatcher(bot)
spam_filter = SpamFilter(limit=10)
spam_filter.init(bot)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    id: int = message.from_user.id
    user = (await manager.create_or_get(UserSettings, user_id=id))[0]
    keyb = create_keyboard(start_keyboard)
    if not user.scens == 'start':
        user.scens = 'start'
        await manager.update(user)
    await message.answer(MESSAGE['start_msg'], reply_markup=keyb)


@dp.message_handler()
async def message(msg: types.Message):
    data = await manager.create_or_get(UserSettings, user_id=msg.from_user.id)
    if msg.text == MESSAGE_KEYBOARD['menu_keyb']:
        data[0].scens = "menu"
        await manager.update(data[0])
        keyb = create_keyboard(menu_keyboard)
        await msg.answer(MESSAGE["menu_msg"], reply_markup=keyb)

    user_spam = spam_filter.user_check(msg.from_user.id)
    if user_spam:
        keyb = create_keyboard(menu_keyboard)
        if not data[0].scens == "menu":
            data[0].scens = "menu"
            await manager.update(data[0])
        await msg.answer(MESSAGE["spam_msg"], reply_markup=keyb)
        return

    await load.init_scene(data[0].scens, manager, data, getter_data).message_handler(msg)


if __name__ == '__main__':
    executor.start_polling(dp)
