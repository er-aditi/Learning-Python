print("It is table of 3:")
for value in range(1, 11):
    data = value * 3

    print("3 * " + str(value) + " = " + str(data))


num = int(input("Enter number: "))

for value in range(1, 11):
    print(num, "*", value, "=", num * value)
