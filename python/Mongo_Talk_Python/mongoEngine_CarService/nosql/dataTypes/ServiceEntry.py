import datetime
import mongoengine


class ServiceEntry(mongoengine.EmbeddedDocument):
    date = mongoengine.DateTimeField(default=datetime.datetime.now)
    description = mongoengine.StringField()
    price = mongoengine.FloatField()
    rating = mongoengine.IntField(min_value=1, max_value=5)