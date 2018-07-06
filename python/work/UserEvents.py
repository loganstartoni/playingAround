import mongoengine

from python.work.Transaction import Tranaction


class UserEvents(mongoengine.document):
    token_print = mongoengine.StringField()
    iat = mongoengine.StringField(required=True)
    user_id = mongoengine.StringField(required=True)

    transaction_list = mongoengine.EmbeddedDocumentListField(Tranaction)

    meta = {
        "db_alias": "dp_logs",
        "collection": "DP_loge_log_events",
        "indexes": [
            {"fields": ["iat", "user_id"], 'unique': True}
        ]
    }