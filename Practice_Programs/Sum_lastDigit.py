digit = int(input("Enter 4 digit Numbers: "))
num_a = digit//10
num_2 = digit % 10
num_b = num_a//10
num_1 = num_b//10

add = num_1 + num_2

print("Add of first and Last Digit: " + str(add))
