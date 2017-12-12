import uuid
import mongoengine

from python.Mongo_Talk_Python.performance_DB_CarService.nosql.DataTypes.engine import Engine
from python.Mongo_Talk_Python.performance_DB_CarService.nosql.DataTypes.service_record import ServiceRecord


class Car(mongoengine.Document):
    model = mongoengine.StringField(required=True)
    make = mongoengine.StringField(required=True)
    year = mongoengine.IntField(required=True)
    mileage = mongoengine.IntField(default=0)
    vi_number = mongoengine.StringField(default=lambda: str(uuid.uuid4()).replace("-", ''))

    engine = mongoengine.EmbeddedDocumentField(Engine, required=True)
    service_history = mongoengine.EmbeddedDocumentListField(ServiceRecord)

    # no need to reference owners here, that is entirely contained in owner class

    meta = {
        'db_alias': 'core',
        'collection': 'cars',
        'indexes': [
        ]
    }
