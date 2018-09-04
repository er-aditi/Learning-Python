print("Enter Number 1, 2, 3, 4")
user = "User Number: "
var = 0
while True:
    var_1 = input(user)
    comp = 5 - int(var_1)
    print("Computer number:  " + str(comp))
    var = int(var) + (int(var_1) + int(comp))
    if var == 20:
        print("Now , 1 Left User Lose the Game")
        break

