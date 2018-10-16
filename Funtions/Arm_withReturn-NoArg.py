num = int(input("Enter Number: "))

origanal = num


def check_armstrong():
    global num
    length = len(str(num))

    result = 0
    while num > 0:
        reminder = num % 10
        result += reminder ** length
        num = num // 10

    if origanal == result:
        return True
    else:
        return False


if check_armstrong():
    print(origanal, "is Armstrong")
else:
    print(origanal, "is not Armstrong")




