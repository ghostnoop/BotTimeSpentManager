from aiogram.dispatcher.filters.state import StatesGroup, State


class ReportStates(StatesGroup):
    get_dates = State()
