import mongoengine
import uuid
import python.Mongo_Talk_Python.mongoEnginePlay.nosql.dataTypes.Engine as Engine
from python.Mongo_Talk_Python.mongoEnginePlay.nosql.dataTypes import ServiceEntry


class Car(mongoengine.Document):

    model = mongoengine.StringField(required=True)
    make = mongoengine.StringField(required=True)
    year = mongoengine.IntField(required=True)
    mileage = mongoengine.FloatField(default=0.0)
    vin_num = mongoengine.StringField(default=lambda: str(uuid.uuid4()).replace('-', ''))

    engine = mongoengine.EmbeddedDocumentField(Engine.Engine)
    service_history = mongoengine.EmbeddedDocumentListField(ServiceEntry.ServiceEntry)

    meta = {
        'db_alias': 'core',
        'collection': 'cars'
    }
