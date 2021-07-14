import aiogram
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from dotenv import load_dotenv, find_dotenv
from aiogram import Bot, Dispatcher
from aiogram.types import ParseMode
from data import config

load_dotenv(find_dotenv())

from utils.misc import chat_bot


async def on_startup(*args):
    import handlers
    import models.base as db
    await db.db_init()
    handlers.setup(dp)


if __name__ == '__main__':
    dp = Dispatcher(chat_bot, storage=MemoryStorage())
    aiogram.executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
