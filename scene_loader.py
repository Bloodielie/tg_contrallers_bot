import os
import importlib.util
from aiogram.types import Message, CallbackQuery
from aiogram import Bot


class BaseScene:
    def __init__(self, bot: Bot, keyboard, lang, manager_db, model_db, getter):
        self.bot = bot
        self.keyboard = keyboard
        self.lang = lang
        self.manager = manager_db
        self.model = model_db
        self.getter = getter

    async def call_handler(self, call: CallbackQuery):
        pass

    async def message_handler(self, message: Message):
        pass


class Loader:
    def __init__(self):
        self.scenes = self.load_scenes()

    def get_scene_by_name(self, scene_name):
        for scene in self.scenes:
            if scene.__module__ == scene_name:
                return scene

    def load_scenes(self):
        scenes = []
        files = [x.replace(".py", "") for x in os.listdir("scenes") if x not in ["__pycache__", "__init__.py"]]
        for file in files:
            scene = self.load_scene(file)
            scene_class = getattr(scene, "Scene")
            scenes.append(scene_class)
        return scenes

    @staticmethod
    def load_scene(file_name):
        spec = importlib.util.spec_from_file_location(file_name, os.path.abspath(f"scenes/{file_name}.py"))
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module

    def init_scene(self, scene_name, bot, keyboard, lang, manager_db, model_db, getter):
        scene = self.get_scene_by_name(scene_name)
        initialized_scene = scene(bot=bot, keyboard=keyboard, lang=lang, manager_db=manager_db, model_db=model_db, getter=getter)
        return initialized_scene
