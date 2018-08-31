
var = 1
active = True

while active:
    num = int(input("Enter NUmber: "))
    if var > num:
        print("Bad Input")
        print("Enter Number Greater than 1")
    else:
        active = False

while var <= num:
    print(var)
    var += 1


