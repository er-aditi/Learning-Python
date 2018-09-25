num = 2
var = 2

while num <= 1000:
    var = 2
    while var < num:
        if num % var == 0:
            break

        var += 1

    if num == var:
        print(str(num) + " is Prime Number")

    num += 1