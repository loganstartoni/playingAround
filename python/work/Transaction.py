import mongoengine


class Tranaction(mongoengine.EmbeddedDocument):
    in_time = mongoengine.StringField()
    transaction_id = mongoengine.StringField()
    elapsed_time = mongoengine.StringField()

    log_massages = mongoengine.ListField(mongoengine.StringField())
