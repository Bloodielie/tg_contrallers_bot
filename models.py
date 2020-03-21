from peewee_asyncext import PostgresqlExtDatabase
import peewee
from configuration.config import Config

config = Config()
database = PostgresqlExtDatabase(config.get_data('app', 'DB_NAME'),
                                 user=config.get_data('app', 'DB_USER'),
                                 host=config.get_data('app', 'DB_HOST'),
                                 password=config.get_data('app', 'DB_PASSWORD'),
                                 register_hstore=False)


class User(peewee.Model):
    class Meta:
        database = database

    user_id = peewee.IntegerField(unique=True)
    time = peewee.IntegerField(default=10800)
    sort = peewee.CharField(default="Время", max_length=20)
    display = peewee.CharField(default="фото", max_length=20)
    city = peewee.CharField(default="brest", max_length=10)
    scens = peewee.CharField(default="start", max_length=20)


User.create_table(True)
database.set_allow_sync(False)
