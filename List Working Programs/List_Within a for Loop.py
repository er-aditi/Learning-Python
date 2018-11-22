cars = ['bmw', 'audi', 'toyota']
cars_1 = ['safari', 'ferrari', 'tarzan']
for car in cars:
    print("I like this car: " + car.title())
    for car_1 in cars_1:
        print(" - ", car_1.title())
