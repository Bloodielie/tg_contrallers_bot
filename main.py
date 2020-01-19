from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher
from scene_loader import Loader
from config import login, password, token, MESSAGE, MESSAGE_KEYBOARD
from database import database, User
from keyboard import Keyboard
import vk_api
import peewee_async
from utils.api_getter import ApiGetter
import logging

logging.basicConfig(filename="error.log", format='\n%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.ERROR)
logger = logging.getLogger(__name__)

bot = Bot(token=token)
dp = Dispatcher(bot)


load = Loader()
keyboard = Keyboard()
manager = peewee_async.Manager(database)
getter_data = ApiGetter('http://127.0.0.1:8000/bus_stop')


vk = vk_api.VkApi(login=login, password=password)
vk.auth()


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    id = message.from_user.id
    await manager.create_or_get(User, user_id=id)
    await message.answer(MESSAGE['start_msg'], reply_markup=keyboard.start_keyboard())


@dp.message_handler()
async def message(msg: types.Message):
    data_ = await manager.create_or_get(User, user_id=msg.from_user.id)
    if not data_[1]:
        if msg.text == MESSAGE_KEYBOARD['start_keyb_kontroler']:
            data_[0].scens = "kontroler"
            await manager.update(data_[0])
            await msg.answer(MESSAGE["kontroler_msg"], reply_markup=keyboard.kontroler_keyboard())
        elif msg.text == MESSAGE_KEYBOARD['start_keyb_settings']:
            data_[0].scens = "settings"
            await manager.update(data_[0])
            await msg.answer(MESSAGE["settings_msg"], reply_markup=keyboard.settings_keyboard())
        elif msg.text == MESSAGE_KEYBOARD['start_keyb_info']:
            await msg.answer(MESSAGE["info_msg"], reply_markup=keyboard.start_keyboard())
        elif msg.text == MESSAGE_KEYBOARD['menu_keyb']:
            await msg.answer(MESSAGE["menu_msg"], reply_markup=keyboard.start_keyboard())
    else:
        await msg.answer('Пиши /start', reply_markup=keyboard.start_keyboard())

    scene = data_[0].scens
    await load.init_scene(scene, bot, keyboard, MESSAGE, manager, User, getter_data).message_handler(msg)


if __name__ == '__main__':
    executor.start_polling(dp)
