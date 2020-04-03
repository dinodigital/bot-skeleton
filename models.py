from peewee import Model, CharField, IntegerField, DateTimeField
from config import DB

from datetime import datetime


class BaseModel(Model):
    class Meta:
        database = DB


class User(BaseModel):
    tg_id = IntegerField()
    username = CharField()
    registered = DateTimeField(default=datetime.now)


# Создание таблиц
DB.create_tables([User, ])
