import mongoengine



def global_init():
    mongoengine.register_connection(alias="core ", host="192.168.1.201", name="demo_dealership")
