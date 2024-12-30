import asyncio
import logging

from classes import TelegramBot, App

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


if __name__ == "__main__":
    try:
        tg = TelegramBot()
        asyncio.run(tg.start_polling())
    except KeyboardInterrupt:
        logger.info(f"EXIT")
else:
    app = App()