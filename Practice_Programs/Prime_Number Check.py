user_input = int(input("Enter Number: "))
var = 2

while var < user_input:
    if user_input % var == 0:
        break

    var += 1

if var == user_input:
    print(str(user_input) + " is Prime Number")
else:
    print(str(user_input) + " is Not Prime Number")