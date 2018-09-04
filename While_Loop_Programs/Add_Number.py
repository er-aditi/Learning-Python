num = int(input("Enter Number: "))
sum_1 = 0
while num > 0:
    sum_1 = sum_1 + (num % 10)
    num = num // 10

print(sum_1)