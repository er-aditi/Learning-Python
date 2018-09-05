num_list = [10, 5, 70, 40, 80, 99, 4, 1111, 7, 25]

smallest = num_list[0]
num = 1
while num < len(num_list):
    if num_list[num] < smallest:
        smallest = num_list[num]
    num += 1

# Largest Number
largest = num_list[0]
num = 1
while num < len(num_list):
    if num_list[num] > largest:
        largest = num_list[num]
    num += 1

diff = largest - smallest

print("Smallest Number is: ", smallest)
print("Largest Number is: ", largest)
print("Difference is: ", diff)


