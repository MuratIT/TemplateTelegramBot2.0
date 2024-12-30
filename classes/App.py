from contextlib import asynccontextmanager

from aiogram.types import Update
from fastapi import FastAPI, Request

from classes import TelegramBot
from settings import BASE_URL, WEBHOOK_PATH

class App(TelegramBot):
    def __init__(self):
        super().__init__()
        self.app = FastAPI(lifespan=self.lifespan)

    @asynccontextmanager
    async def lifespan(self, app: FastAPI):
        app.add_api_route(WEBHOOK_PATH, endpoint=self.webhook, methods=['POST'])

        await self.bot.set_webhook(url=f"{BASE_URL}{WEBHOOK_PATH}",
                                    allowed_updates=self.dp.resolve_used_update_types(),
                                    drop_pending_updates=True)
        yield
        await self.bot.delete_webhook(drop_pending_updates=True)

    async def webhook(self, request: Request):
        update = Update.model_validate(await request.json(), context={"bot": self.bot})
        await self.dp.feed_update(self.bot, update)


