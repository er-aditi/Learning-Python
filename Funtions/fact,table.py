num = int(input("Enter Number: "))


def check_even():
    if num % 2 == 0:
        table()
    else:
        factorial()


def table():
    for var in range(1, 11):
        print(str(num) + " * " + str(var) + " = " + str(num * var))


def factorial():
    value = 1
    for var in range(num, 0, -1):
        value = value * var

    print("Factorial of " + str(num) + " is " + str(value))


check_even()

