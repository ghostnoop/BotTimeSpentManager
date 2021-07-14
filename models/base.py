from tortoise.models import Model
from tortoise import fields, Tortoise

from data import config


class Client(Model):
    id = fields.BigIntField(pk=True, generated=False)
    nickname = fields.CharField(max_length=255, default=None, null=True)
    created_at = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "client"


class Event(Model):
    id = fields.BigIntField(pk=True, generated=True)
    client = fields.ForeignKeyField('models.Client', related_name='events')

    name = fields.CharField(max_length=255, default=None, null=True)
    start_at = fields.DatetimeField(auto_now_add=True)
    end_at = fields.DatetimeField(default=None, null=True)
    sum_time = fields.BigIntField(default=None,null=True)

    class Meta:
        table = "event"


async def db_init():
    await Tortoise.init(
        db_url=config.get_db(),
        modules={'models': ['models.base']}
    )
    # Generate the schema
    await Tortoise.generate_schemas()
