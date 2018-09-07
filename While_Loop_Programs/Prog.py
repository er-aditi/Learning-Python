num = 1
val = 1

while num <= 5:
    var = 1

    while var <= 5:
        if var <= val:
            print(val, end=" ")
        else:
            print(" ")

        var += 1
    val += 1
    print("")
    num += 1