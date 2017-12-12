import mongoengine


def global_init():
    mongoengine.register_connection(alias="core", host="hermione", port=27017, name="demo_dealership")
