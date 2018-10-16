num = int(input("Enter Number: "))


def check_armstrong():
    global num
    length = len(str(num))
    origanal = num
    result = 0
    while num > 0:
        reminder = num % 10
        result += reminder ** length
        num = num // 10

    if origanal == result:
        print(origanal, "is Armstrong")
    else:
        print(origanal, "is not Armstrong")


check_armstrong()


