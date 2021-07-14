from aiogram import types
from aiogram.dispatcher import FSMContext

from data import messages
from models.base import Event
from states.EventStates import EventStates
from utils.misc import chat_bot


async def end_event(callback: types.CallbackQuery, state: FSMContext):
    await EventStates.next()
    event_id = int(callback.data.split("::")[1])
    await state.update_data({'event_id': event_id})
    await chat_bot.send_message(callback.from_user.id, messages.CREATED_EVENT_GET_NAME, reply_markup=None)
