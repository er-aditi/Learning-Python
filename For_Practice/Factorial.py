num = int(input("Enter Number: "))

var = 1
if num >= 1:
    for val in range(1, num+1):
        var = val * var

    print(var)

