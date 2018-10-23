condition = input("Enter S or M or P or D: ")


def total():
    first = int(input("Enter First Number: "))
    second = int(input("Enter Second Number: "))
    return first + second


def minus():
    first = int(input("Enter First Number: "))
    second = int(input("Enter Second Number: "))
    return first - second


def product():
    first = int(input("Enter First Number: "))
    second = int(input("Enter Second Number: "))
    return first * second


def division():
    first = int(input("Enter First Number: "))
    second = int(input("Enter Second Number: "))
    return first / second


if condition == "S" or condition == 's':
    print("Sum is: " + str(total()))
elif condition == "M" or condition == 'm':
    print("Subtraction is: " + str(minus()))
elif condition == "P" or condition == 'p':
    print("Product is: " + str(product()))
elif condition == "D" or condition == 'd':
    print("Division is: " + str(division()))
else:
    print("Sorry!, Wrong Input.")

