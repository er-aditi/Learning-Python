num = 500
while 1 < num:
    num_1 = num % 10
    use = num // 10
    num_2 = int(use) % 10
    num_3 = int(use) // 10

    result = (num_1 * num_1 * num_1) + (num_2 * num_2 * num_2) + (num_3 * num_3 * num_3)
    if result == num:
        print(str(num) + " is Armstrong")

    num -= 1

