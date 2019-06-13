class Car(object):

    def __init__(self):
        print("Start base class")

    def drive(self):
        print("Lets start")

    def stop(self):
        print("Lets stop.........")



class BMW(Car):

    def __init__(self):
        Car.__init__(self)
        print("*****************")

    def drive(self):
        super().drive()
        print("Its new")


    def test(self):
        print("LEts see")


c = Car()
c.drive()
c.stop()


b = BMW()
b.drive()
b.test()
b.stop()