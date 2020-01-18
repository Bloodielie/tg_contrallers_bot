import aiohttp


class ApiGetter:
    def __init__(self, short_url):
        self.url = short_url
        self.s = aiohttp.ClientSession()

    async def get_data_bus(self, type: str, **kwargs):
        url = f'{self.url}/{type}'
        async with self.s.get(url, params=kwargs) as response:
            return self.dict_in_list(await response.json())

    @staticmethod
    def dict_in_list(date: dict):
        temporary_data = []
        for data in date.keys():
            inform = date.get(data)
            _tuple = (data, [inform[0], inform[1]])
            temporary_data.append(_tuple)
        return temporary_data
