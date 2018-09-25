num = 1
while num <= 500:
    num_1 = num % 10
    use_1 = num // 10
    num_2 = use_1 % 10
    num_3 = use_1 // 10

    result = (num_1 * num_1 * num_1) + (num_2 * num_2 * num_2) + (num_3 * num_3 * num_3)

    if result == num:
        print(str(num) + " is Armstrong")

    num += 1