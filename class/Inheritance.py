class Car(object):

    def __init__(self):
        print("Inheritance parent class")

    def start(self):
        print("Started......")

    def stop(self):
        print("Stop...")



class BMW(Car):
    print("It is child class inherit the properties of car")

c = Car()
c.start()
c.stop()

b = BMW()
b.stop()
b.start()