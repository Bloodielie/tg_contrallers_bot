import asyncio
from aiogram import Bot


class SpamFilter:
    def __init__(self, limit, delay=60):
        self.limit = limit
        self.delay = delay
        self.users_requests = {}
        self.active = True

    def init(self, bot: Bot) -> None:
        bot.loop.create_task(self._run_timer())

    def _add_request(self, user_id) -> None:
        user_id = str(user_id)
        if self.users_requests.get(user_id):
            self.users_requests[user_id] += 1
        else:
            self.users_requests[user_id] = 1

    def _check_limit(self, user_id) -> bool:
        user_id = str(user_id)
        if self.users_requests.get(user_id) and self.users_requests[user_id] > self.limit:
            return True
        return False

    def user_check(self, user_id):
        self._add_request(user_id)
        return self._check_limit(user_id)

    def _clear_users_requests(self) -> None:
        self.users_requests = {}

    async def _run_timer(self) -> None:
        while self.active:
            self._clear_users_requests()
            await asyncio.sleep(self.delay)
