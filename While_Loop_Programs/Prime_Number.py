num = int(input("Enter Number: "))
var = 2

while var <= num:
    if num % var == 0:
        break

    var += 1

if int(num) == int(var):
    print("Prime Number ", num)
else:
    print("Not a Prime Number: ", num)

