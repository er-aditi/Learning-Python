number = input("Please enter a number. To find that number is even or odd? ")
print(int(number))
if int(number) % 2 == 0:
    print("The Number " + str(number) + " is even")
else:
    print("The Number " + str(number) + " is Odd")