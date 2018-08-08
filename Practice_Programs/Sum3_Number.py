num = input("Please Enter 3 Number: ")
digit = int(num) // 10
last = int(num) % 10
mid = digit % 10
first = digit // 10
sum_1 = first + mid + last
print(" Number is: " + str(first) + " + " + str(mid) + " + " + str(last) + " = " + str(sum_1))

