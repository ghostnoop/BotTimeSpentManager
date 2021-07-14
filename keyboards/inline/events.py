from aiogram import types


async def created_event_buttons(event_id: int):
    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(types.InlineKeyboardButton("Закончить событие", callback_data=f"event::{event_id}"))

    return keyboard
