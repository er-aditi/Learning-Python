num = int(input("Enter Number: "))
var = 2
active = True
while True:
    if num % 2 == 0 and num != 2:
        print("Number is not Prime")
        break

    while var < num:
        if num % var != 0:
            print("Number is Prime: ", num)
            num += 1
    active = False