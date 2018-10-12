num = int(input("Enter Number: "))


def is_prime(num1):
    var = 2
    while num1 > var:
        if num1 % var == 0:
            break
        var += 1

    if num1 == var:
        return True
    else:
        return False


if is_prime(num):
    print(num, "is Prime")
else:
    print(num, "is not Prime")



