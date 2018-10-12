# with arg no return
num = int(input("Enter Number: "))


def prime(num1):
    var = 2
    while num1 > var:
        if num1 % var == 0:
            break
        var += 1

    if num1 == var:
        print(num1, "is Prime")
    else:
        print(num1, "is not Prime")


prime(num)