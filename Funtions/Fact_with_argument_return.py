#  with argument no return value
num = int(input("Enter number: "))


def fact(num1):
    var = 1
    for index in range(num1, 0, -1):
        var = var * index
    print("Factorial of", num, "is", var)


fact(num)