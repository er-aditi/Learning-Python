num = int(input("Enter number: "))
count = 1
for var in range(num, num * 11, num):
    print(str(num) + " * " + str(count) + " = " + str(var))
    count += 1
