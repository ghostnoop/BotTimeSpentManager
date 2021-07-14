from aiogram import types
from aiogram.dispatcher import FSMContext

from data import messages
from keyboards.default.events import get_event_buttons
from models.base import Client
from utils.misc import chat_bot


async def bot_start(message: types.Message, state: FSMContext):
    await Client.update_or_create(id=message.from_user.id, defaults={"nickname": message.from_user.username})
    keyboard = await get_event_buttons()
    await chat_bot.send_message(message.from_user.id, text=messages.HELLO, reply_markup=keyboard)
