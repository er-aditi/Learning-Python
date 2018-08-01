num_1 = range(1, 11)
for value in num_1:
    print(value)

print(list(num_1))

comprehensions_1 = [value**2 for value in num_1]
print(comprehensions_1)

for number in comprehensions_1:
    print(number)
