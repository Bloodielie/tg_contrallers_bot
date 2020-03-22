import os
import importlib.util
from aiogram.types import Message, CallbackQuery
from aiogram import Bot


class BaseScene:
    def __init__(self, manager_db, user_data, getter):
        self.manager = manager_db
        self.user_data = user_data
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

    def init_scene(self, scene_name, manager_db, user_data, getter):
        scene = self.get_scene_by_name(scene_name)
        initialized_scene = scene(manager_db=manager_db, user_data=user_data, getter=getter)
        return initialized_scene
