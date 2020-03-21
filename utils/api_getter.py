import aiohttp


class ApiGetter:
    def __init__(self, domen: str, api_prefix: str = 'api'):
        self.url = f'{domen}/{api_prefix}'
        self.s = aiohttp.ClientSession()

    async def get_date(self, method: str, type_return: str = 'dict', **kwargs):
        async with self.s.get(f'{self.url}/{method}', params=kwargs) as response:
            if type_return == 'list':
                return self.dict_in_list(await response.json())
            return await response.json()

    @staticmethod
    def dict_in_list(date: dict) -> list:
        temporary_data = []
        for data in date.keys():
            inform = date.get(data)
            _tuple = (data, [inform[0], inform[1]])
            temporary_data.append(_tuple)
        return temporary_data
