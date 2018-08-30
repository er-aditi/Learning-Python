num = int(input("Enter number: "))
var = 1
active = True
while num:
    if var <= num:
        print(var)
        var += 1
    else:
        print("Bad Input\n Enter Number Greater than 1")