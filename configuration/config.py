from configuration.utils import AbstractConfig


class Config(AbstractConfig):
    def __init__(self):
        self.config_path = 'configuration/settings.ini'
        super().__init__(self.config_path)

    def get_data(self, section: str, configuration_name: str):
        return self.config.get(section, configuration_name)
