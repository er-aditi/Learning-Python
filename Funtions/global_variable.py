# local variable
n = 10


def fun1():
    n = 70  # global variable
    print(n)


def fun2():
    print(n)
    fun1()


fun2()



