def func1():
    n = 10
    print(n)


def func2():
    n = 20
    print(n)
    func1()


def func3():
    n = 30
    print(n)
    func2()


# main method
func3()

