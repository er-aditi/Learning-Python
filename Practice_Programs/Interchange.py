# num_1 = input("Enter 1 Number ")
# print("num_1 = " + str(num_1))
# num_2 = input("Enter no 2: ")
# print("num_2 = " + str(num_2))
#
# num_3 = num_1
# num_1 = num_2
# num_2 = num_3
#
# print("\nAfter interchange\n")
#
# print("num_1 = " + str(num_1))
# print("num_2 = " + str(num_2))

# in Pyhton
num_1 = int(input("Enter num 1: "))
num_2 = int(input("Enter num 2: "))
num_1, num_2 = num_2, num_1
print("After swap")
print(num_1)
print(num_2)
