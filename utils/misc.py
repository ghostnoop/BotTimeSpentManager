from aiogram import Bot
from aiogram.types import ParseMode

from data import config

chat_bot = Bot(config.get_token(), parse_mode=ParseMode.HTML, validate_token=True)
