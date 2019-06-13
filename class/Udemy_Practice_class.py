class Fruit(object):

    def __init__(self):
        print("Variety of fruits")

    def nutrition(self):
        print("It specify nutrition of class")

    def fruit_shape(self):
        print("It specify shapes of fruit")


class Kiwi(Fruit):

    def __init__(self):
        Fruit.__init__(self)
        print("My favorite fruit is KIWI")

    def nutrition(self):
        print("Very Healthy")

    def color(self):
        print("Green")


f = Fruit()
f.nutrition()
f.fruit_shape()
print("* " * 20)
k = Kiwi()
k.nutrition()
k.color()
k.fruit_shape()


