import json

class JsonUtils:
    def __init__(self, file_path):
        self.file_path = file_path

    def get_json(self):
        with open(self.file_path, 'r', encoding='utf-8') as file:
            return json.load(file)

    def write_json(self, data, indent=4, ensure_ascii=None, sort_keys=None):
        with open(self.file_path, 'r', encoding='utf-8') as file:
            data_json = json.load(file)
        with open(self.file_path, 'w', encoding='utf-8') as file:
            data_json.update(data)
            json.dump(data_json, file, indent=indent, sort_keys=sort_keys, ensure_ascii=ensure_ascii)
