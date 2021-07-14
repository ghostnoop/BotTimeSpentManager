from aiogram.dispatcher.filters.state import StatesGroup, State


class EventStates(StatesGroup):
    event_in_process = State()
    event_get_name = State()
