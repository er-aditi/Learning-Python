num = 1

while num <= 5:

    val = 1
    var = 1
    while var <= 5:
        if val % 2 == 0:
            num_1 = 0
        else:
            num_1 = 1

        print(num_1, end=" ")
        val += 1
        var += 1
    print("")
    num += 1