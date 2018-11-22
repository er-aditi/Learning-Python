first = int(input("Enter table number "))


def multiply(a, b):
    print(a, "*", b, "=", a*b)


for var in range(1, 11):
    multiply(first, var)