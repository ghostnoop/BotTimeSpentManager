import asyncio
from datetime import datetime, timedelta, timezone
from bot import *
from models.base import Event
from utils.time_utils import get_dates_from_str


async def worker():
    import models.base as db
    await db.db_init()

    first, second = await get_dates_from_str("20/06/2021 20/08/2021")
    events = await Event.filter(start_at__gte=first, end_at__lte=second)
    print(events)


if __name__ == '__main__':
    asyncio.run(worker())
