age = 18
if age < 4:
    print("Its entry fee is Free".title())
elif age < 18:
    print("Its entry fee is 5")
else:
    print("Its entry fee is 10")


# In single print

age = 13
if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10

print("Its Entry Fee is: " + str(price))
