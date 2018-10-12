num = 1
var = int(input("Enter Number: "))


def table():

    global num
    print(num * var)
    num += 1
    if num <= 10:
        table()


table()


