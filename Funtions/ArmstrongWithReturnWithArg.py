num = int((input("Enter Number: ")))


def is_armstrong(value):
    length = len(str(value))
    origanal = value
    result = 0
    while value > 0:
        reminder = value % 10
        result += reminder ** length
        value = value//10

    if origanal == result:
        return True
    else:
        return False


if is_armstrong(num):
    print(num, "is Armstrong")
else:
    print(num, "Is not Armstrong")


