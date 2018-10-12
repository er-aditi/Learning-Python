# No Arg NO Return Value
num = int(input("Enter Number: "))


def fact():
    var = 1
    for index in range(num, 0, -1):
        var = index * var
    print(var)


fact()
