# • Admission for anyone under age 4 is free.
# • Admission for anyone between the ages of 4 and 18 is $5.
# • Admission for anyone age 18 or older is $10.

age = 15
if age < 4:
    price = 0
elif age < 18 or age > 65:
    price = 5
else:
    price = 10

print("If MY age is " + str(age) + ". Then Price is: "+str(price))