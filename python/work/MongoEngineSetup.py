import mongoengine


def global_init():
    mongoengine.register_connection(alias="dp_logs", port=27017, name="DataPower_loga")
