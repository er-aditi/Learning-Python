num = int(input("Enter Number: "))


def check_armstrong(value):
    length = len(str(value))
    origanal = value
    result = 0
    while value > 0:
        reminder = value % 10
        result += reminder ** length
        value = value // 10

    if origanal == result:
        print(origanal, " is Armstrong")
    else:
        print(origanal, "is not Armstrong")


check_armstrong(num)