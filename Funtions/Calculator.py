condition = input("Enter 'S' or 'M' or 'P' or 'D': ")


def total():
    first = int(input("Enter First Number: "))
    second = int(input("Enter Second Number: "))
    total_sum = first + second
    print("Total = " + str(total_sum))


def division():
    first = int(input("Enter First Number: "))
    second = int(input("Enter Second Number: "))
    division_1 = first / second
    print(" Division = " + str(division_1))


def minus():
    first = int(input("Enter First Number: "))
    second = int(input("Enter Second Number: "))
    minus_1 = first - second
    print("Minus = " + str(minus_1))


def product():
    first = int(input("Enter First Number: "))
    second = int(input("Enter Second Number: "))
    print("Product = ", first * second)


if condition == "M" or condition == "m":
    minus()
elif condition == "S" or condition == 's':
    total()
elif condition == "P" or condition == 'p':
    product()
elif condition == 'D' or condition == 'd':
    division()
else:
    print("Sorry Wrong Input")