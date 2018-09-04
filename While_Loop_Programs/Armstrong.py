num = int(input("Enter Number: "))
num_1 = num % 10
use = num // 10
num_2 = int(use) % 10
num_3 = int(use) // 10

result = (num_1 * num_1 * num_1) + (num_2 * num_2 * num_2) + (num_3 * num_3 * num_3)
print(result)

if result == num:
    print("Number is Armstrong")
else:
    print("Number is not Armstrong")



