from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.redis import RedisStorage

from settings import TOKEN, REDIS_URL

from .Loading import LoadingModule, LoadingMiddlewares

class TelegramBot:
    def __init__(self):
        self.bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
        storage = RedisStorage.from_url(REDIS_URL)
        self.dp = Dispatcher(storage=storage)

        loading_middlewares = LoadingMiddlewares()
        loading_middlewares.load_middlewares(self.dp)

        loading_module = LoadingModule()
        loading_module.load_modules(self.bot, self.dp)

    async def start_polling(self):
        await self.bot.delete_webhook(drop_pending_updates=True)
        await self.dp.start_polling(self.bot)

