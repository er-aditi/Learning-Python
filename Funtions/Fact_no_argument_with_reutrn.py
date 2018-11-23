# no argument with return value
num = int(input("Enter Number: "))


def fact():
    var = 1
    for index in range(num, 0, -1):
        var = var * index
    return var


value = fact()
print(value)
