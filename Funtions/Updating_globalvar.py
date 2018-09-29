var = 10


def fun1():
    global var
    for var in range(var, 100):
        var = var+1
        print("Fun1 value is ", var)


fun1()