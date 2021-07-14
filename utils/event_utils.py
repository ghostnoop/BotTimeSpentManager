from models.base import Event
from utils.time_utils import from_dt_to_hours_minutes


async def event_to_text(event: Event):
    hours, minutes, seconds = await from_dt_to_hours_minutes(event.sum_time)
    return f"Название: <b>{event.name}</b>\nПродолжительность: <i>{hours} часов, {minutes} минут, {seconds} секунд</i>"
