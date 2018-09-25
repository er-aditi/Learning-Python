num = int(input("Enter Num: "))

for var in range(num, num * 11, num):
    # print(str(num) + " * " + " = " + str(var))
    print(str(var) + " * " + str((var//num)) + " = " + str(num))