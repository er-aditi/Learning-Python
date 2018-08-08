num = input("Please Enter 3 Number: ")
print(int(num))
digit = int(num) // 10
last = int(num) % 10
mid = digit % 10
first = digit // 10
sum_1 = first + mid + last
print(" Number is: " + str(first) + " + " + str(mid) + " + " + str(last) + " = " + str(sum_1))

# Reverse
rev = int(last) * 100 + int(mid) * 10 + int(first)
print(int(rev))

# Palindrome

if int(num) == int(rev):
    print("it is Palindrome")
else:
    print("It is not a palindrome")
