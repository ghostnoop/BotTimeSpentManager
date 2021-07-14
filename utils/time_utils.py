from datetime import datetime, timezone


async def from_dt_to_hours_minutes(dt: int):
    hours = dt // 3600
    seconds = hours * 3600
    current_seconds = dt - seconds
    minutes = current_seconds // 60
    seconds = current_seconds - minutes * 60
    return hours, minutes, seconds


def utc_to_local(utc_dt):
    return utc_dt.replace(tzinfo=timezone.utc).astimezone(tz=None)


def local_to_utc(date: datetime):
    return date.astimezone(tz=timezone.utc)


async def get_dates_from_str(s: str):
    try:
        a, b = s.split(' ')
        first = local_to_utc(datetime.strptime(a, '%d/%m/%Y'))
        second = local_to_utc(datetime.strptime(b, '%d/%m/%Y'))
        return first, second
    except Exception as e:
        print(e)
        return None, None
