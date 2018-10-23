num = int(input("Enter Number: "))


def is_even():
    if num % 2 == 0:
        return True
    else:
        return False


if is_even():
    print("Number is Even")
else:
    print("Number is Odd")