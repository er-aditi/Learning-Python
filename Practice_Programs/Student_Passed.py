a = int(input("Enter marks in A: "))
b = int(input("Enter Marks in B: "))

if a >= 55 and b >= 45:
    print("Student is Pass")

elif (a >= 45) and (a <= 55) and (b >= 55):
    print('Student is Passed')

elif b <= 45 and a >= 65:
    print("Appear in B")
else:
    print("He is Failed")
