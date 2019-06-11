class Car(object):

    wheel = 4

    def __init__(self, make, model):
        self.make = make
        self.model = model

    def info(self):
        print("The make of car is: ", self.make)
        print("The model of car is: ", self.model)

c1 = Car('bmw', 501)
c1.info()
print(c1.wheel)

c2 = Car('eze', 'i522')
c2.info()