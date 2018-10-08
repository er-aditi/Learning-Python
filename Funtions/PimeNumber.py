user = int(input("Enter Number: "))


def is_check_prime():
    num = 2
    while user > num:
        if user % num == 0:
            break

        num += 1

    if user == num:
        return True
    else:
        return False


if is_check_prime():
    print(user, "is Prime")
else:
    print(user, "is not prime")
