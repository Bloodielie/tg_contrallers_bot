from peewee_asyncext import PostgresqlExtDatabase
import peewee
from config import db_name, user, host, password_db

database = PostgresqlExtDatabase(db_name, user=user, host=host, password=password_db, register_hstore=False)


class User(peewee.Model):
    class Meta:
        database = database

    user_id = peewee.IntegerField(unique=True)
    time = peewee.IntegerField(default=10800)
    sort = peewee.CharField(default="Время", max_length=20)
    display = peewee.CharField(default="Фото", max_length=20)
    scens = peewee.CharField(default="kontroler", max_length=20)
    city = peewee.CharField(default="brest", max_length=10)


User.create_table(True)
database.set_allow_sync(False)
