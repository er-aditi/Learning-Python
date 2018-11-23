num1 = int(input("Enter 1st Number: "))
num2 = int(input("Enter 2nd Number: "))


def add1():
    var = num1 + num2
    return var


def add2():
    var1 = num1 + num2
    print(var1)


sum1 = add1()
print(sum1)

add2()