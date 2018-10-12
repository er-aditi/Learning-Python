# No Arg No Return
num = int(input("Enter Number: "))


def check_prime():
    var = 2
    while num > var:
        if num % var == 0:
            break

        var += 1

    if num == var:
        print(num, "is Prime Number")
    else:
        print(num, "is not Prime Number")


check_prime()