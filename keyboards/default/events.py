from aiogram import types

from data import strings


async def get_event_buttons():
    keyboard = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
    keyboard.add(strings.CREATE_EVENT)
    keyboard.add(strings.GET_REPORT_OF_WEEK)
    keyboard.add(strings.GET_REPORT_CUSTOM)

    return keyboard
