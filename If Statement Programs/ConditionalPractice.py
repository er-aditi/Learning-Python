# Tests for equality and inequality with strings
name = 'Aditi'
print(name == 'aditi')
if name == 'aditii':
    print("It is correct")
    name = 'jain'
print(name == 'jain')

# Tests using the lower() function
if name.lower() == 'aditi':
    print(name)

print(name.lower() == 'aditi')

# • Numerical tests involving equality and inequality, greater than and
# less than, greater than or equal to, and less than or equal to

num = 58
print(num == 56)
print(num == 58)
print(num <= 55)
if num >= 58:
    print(" it is true")
else:
    print("You are correct")

# Tests using the and keyword and the or keyword
print(num)
if num == 34 and num <= 55:
    print(" and operator  ")

if num == 56 or num <= 99:
    print("or operator")

# Test whether an item is in a list
values = [1, 5, 9, 88]
for value in values:
    if value == 5:
        print("data in correct")
    else:
        print("data not mismatched")

# Test whether an item is not in a list
value = 1
if value not in values:
    if value == 65:
        print("data mismatched")