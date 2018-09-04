num = int(input("Enter Number: "))
val = int(input("Enter Power: "))
var = 1

while 1 <= val:
    var = var * num
    val -= 1

print(var)
