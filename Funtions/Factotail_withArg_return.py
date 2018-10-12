# with Argument with return type
num = int(input("Enter Number: "))


def fact(num1):
    value = 1
    for index in range(num1, 0, -1):
        value = index * value
    return value


var = fact(num)
print(var)