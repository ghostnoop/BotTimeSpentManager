import os


def get_token():
    BOT_TOKEN = os.environ.get("TOKEN", "")
    print(BOT_TOKEN)
    return BOT_TOKEN


def get_db():
    DB_USER = os.environ.get("DB_USER")
    DB_PASSWORD = os.environ.get("DB_PASSWORD")
    DB_HOST = os.environ.get("DB_HOST")
    DB_PORT = os.environ.get("DB_PORT")
    DB_NAME = os.environ.get("DB_NAME")
    DB_DRIVER = os.environ.get("DB_DRIVER")

    s= f"{DB_DRIVER}://{DB_USER}:{DB_PASSWORD}@db.{DB_HOST}:{DB_PORT}/{DB_NAME}"
    print(s)
    return s
