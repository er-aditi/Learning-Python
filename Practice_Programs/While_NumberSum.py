num = int(input("Enter Number: "))

var = 0

while num > 1:
    var = var + (num % 10)
    num = num // 10

print(var)
