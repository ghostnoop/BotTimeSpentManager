from aiogram import Dispatcher
from aiogram.dispatcher.filters import CommandStart

from data import strings
from handlers.basic import bot_start
from handlers.inline import end_event
from handlers.text import create_event, event_get_name, report_custom, dates_report_custom
from states.EventStates import EventStates
from states.ReportStates import ReportStates


def setup(dp: Dispatcher):
    dp.register_message_handler(bot_start, CommandStart(), state='*')
    dp.register_message_handler(create_event, lambda message: message.text == strings.CREATE_EVENT, state='*')
    dp.register_callback_query_handler(end_event, lambda callback: callback.data.split("::")[0] == "event",
                                       state=EventStates.event_in_process)

    dp.register_message_handler(event_get_name, lambda message: message, state=EventStates.event_get_name)

    dp.register_message_handler(report_custom, lambda message: message.text == strings.GET_REPORT_CUSTOM, state='*')
    dp.register_message_handler(dates_report_custom, lambda message: message, state=ReportStates.get_dates)
