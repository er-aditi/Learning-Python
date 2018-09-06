num = 2
index = 1
while num <= 500:
    var = 2
    while var < num:
        if num % var == 0:
            break
        var += 1

    if num == var:
        print(str(index) + ". Number is Prime: ", num)
        index += 1

    num += 1