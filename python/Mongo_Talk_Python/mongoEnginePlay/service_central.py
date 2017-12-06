from python.Mongo_Talk_Python.mongoEnginePlay.nosql.dataTypes.ServiceEntry import ServiceEntry
from python.Mongo_Talk_Python.mongoEnginePlay.nosql.mongo_setup import global_init
from python.Mongo_Talk_Python.mongoEnginePlay.nosql.dataTypes.Car import Car
from python.Mongo_Talk_Python.mongoEnginePlay.nosql.dataTypes.Engine import Engine


def main():
    print_header()
    config_mongo()
    user_loop()


def print_header():
    print('----------------------------------------------')
    print('|                                             |')
    print('|           SERVICE CENTRAL v.02              |')
    print('|               demo edition                  |')
    print('|                                             |')
    print('----------------------------------------------')
    print()


def config_mongo():
    global_init()


def user_loop():
    while True:
        print("Available actions:")
        print(" * [a]dd car")
        print(" * [l]ist cars")
        print(" * [f]ind car")
        print(" * perform [s]ervice")
        print(" * e[x]it")
        print()
        ch = input("> ").strip().lower()
        if ch == 'a':
            add_car()
        elif ch == 'l':
            list_cars()
        elif ch == 'f':
            find_car()
        elif ch == 's':
            service_car()
        elif not ch or ch == 'x':
            print("Goodbye")
            break


def add_car():
    # print("TODO: add_car")
    """
    model = mongoengine.StringField()
    make = mongoengine.StringField()
    year = mongoengine.IntField()
    mileage = mongoengine.FloatField()
    vin_num = mongoengine.StringField()

    :return:
    """

    model = input("What is the model?")
    make = input("What is the make?")
    year = int(input("What is the modal year?"))
    # mileage = float(input("What is the mileage?"))
    # vin_num = input("What is the vin?")

    car = Car()
    car.model = model
    car.make = make
    car.year = year
    # car.mileage = mileage
    # car.vin_num = vin_num

    engine = Engine()
    engine.horsepower = 600
    engine.mpg = 20
    engine.liters = 5.0

    car.engine = engine

    car.save()


def list_cars():
    cars = Car.objects().order_by("year")
    for car in cars:
        print(f"Make:{car.make} -- Model:{car.model} -- vin:{car.vin_num} (year:{car.year})")
        print(f"\t There are {len(car.service_history)} service Records.")
        for entry in car.service_history:
            print(f"\t   {entry.date} -- {entry.description} -- {entry.price:,.0f}")
    print()


def find_car():
    vin = input("what is the VIN?")
    car = Car.objects().filter(vin_num=vin).first()
    if not car:
        print(f"Car with {car.vin_num} NOT found.")
    else:
        print(f"Make:{car.make} -- Model:{car.model} -- vin:{car.vin_num} (year:{car.year})")
        print(f"\t There are {len(car.service_history)} service Records.")
        for entry in car.service_history:
            print(f"\t   {entry.date} -- {entry.description} -- {entry.price}")
        print()


def service_car():
    # long way is not thread safe.
    # vin = input("what is the VIN?")
    # car = Car.objects().filter(vin_num=vin).first()
    # if not car:
    #     print(f"Car with {car.vin_num} NOT found.")
    #     return
    # else:
    #     print(f"Make:{car.make} -- Model:{car.model} -- vin:{car.vin_num} (year:{car.year})")
    #     print(f"\t There are {len(car.service_history)} service Records.")
    #
    #     service_record = ServiceEntry()
    #     service_record.price = float(input("What is the Price?"))
    #     service_record.description = input("What was done?")
    #     service_record.rating = int(input("What is the customer rating?"))
    #
    #     car.service_history.append(service_record)
    #     car.save()

    vin = input("what is the VIN?")

    service_record = ServiceEntry()
    service_record.price = float(input("What is the Price?"))
    service_record.description = input("What was done?")
    service_record.rating = int(input("What is the customer rating?"))

    updated = Car.objects(vin_num=vin).update_one(push__service_history=service_record)
    if updated == 0:
        print(f"Car with {vin} NOT found.")




if __name__ == '__main__':
    main()
