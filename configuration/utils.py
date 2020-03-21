from typing import Union
from configparser import NoSectionError, NoOptionError, ConfigParser
from abc import ABC, abstractmethod


class AbstractConfig(ABC):
    def __init__(self, config_path: str):
        self.config = ConfigParser()
        self.config.read(config_path)

    @abstractmethod
    def get_data(self, section: str, configuration_name: str) -> Union[str, NoSectionError, NoOptionError]:
        pass
