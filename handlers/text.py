from datetime import datetime

from aiogram import types
from aiogram.dispatcher import FSMContext
from tortoise import timezone
from datetime import timezone as tz
from data import messages
from keyboards.default.events import get_event_buttons
from keyboards.inline.events import created_event_buttons
from models.base import Event
from states.EventStates import EventStates
from states.ReportStates import ReportStates
from utils.event_utils import event_to_text
from utils.misc import chat_bot
from utils.time_utils import from_dt_to_hours_minutes, utc_to_local, get_dates_from_str


async def create_event(message: types.Message, state: FSMContext):
    event = await Event.create(client_id=message.from_user.id)
    keyboard = await created_event_buttons(event.id)
    await EventStates.event_in_process.set()

    now = utc_to_local(event.start_at).strftime('%H:%M:%S - %d/%m/%Y')
    await chat_bot.send_message(message.from_user.id,
                                messages.CREATED_EVENT.format(event.id, now),
                                reply_markup=keyboard)


async def event_get_name(message: types.Message, state: FSMContext):
    data = await state.get_data()
    event = await Event.get(id=data['event_id'])

    event.name = message.text
    event.end_at = timezone.now()
    event.sum_time = (event.end_at - event.start_at).seconds

    await event.save()

    hours, minutes, seconds = await from_dt_to_hours_minutes(event.sum_time)
    await state.finish()
    await chat_bot.send_message(message.from_user.id,
                                messages.END_EVENT_WITH_NAME.format(event.name,
                                                                    hours, minutes, seconds
                                                                    ), reply_markup=await get_event_buttons())


async def report_custom(message: types.Message, state: FSMContext):
    await ReportStates.get_dates.set()

    await chat_bot.send_message(message.from_user.id, text=messages.CUSTOM_DATE_REPORT)


async def dates_report_custom(message: types.Message, state: FSMContext):
    first, second = await get_dates_from_str(message.text)
    if first is None:
        return

    events = await Event.filter(start_at__gte=first, end_at__lte=second)
    s = ""
    sum_final = 0
    for event in events:
        s += await event_to_text(event) + "\n"
        sum_final += event.sum_time

    hours, minutes, seconds = await from_dt_to_hours_minutes(sum_final)
    s += f"Всё заняло: <i>{hours} часов, {minutes} минут, {seconds} секунд</i>"

    await chat_bot.send_message(message.from_user.id, s, reply_markup=await get_event_buttons())
