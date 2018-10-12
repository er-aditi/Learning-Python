# no ARG With Return
num = int(input("Enter Number: "))


def is_prime():
    var = 2
    while num > var:
        if num % var == 0:
            break
        var += 1
    if num == var:
        return True
    else:
        return False


if is_prime():
    print(num, "is Prime")
else:
    print(num, "is not Prime")


