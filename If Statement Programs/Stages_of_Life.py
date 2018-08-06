age = 500
if age < 2:
    print("The Person is baby of age: " + str(age))
elif age < 4:
    print("The Person is toddler of age: " + str(age))
elif age < 13:
    print("The Person is Kid of age: " + str(age))
elif age < 20:
    print("The Person is teenager of age: " + str(age))
elif age < 65:
    print("The Person is Adult of age: " + str(age))
else:
    print("The Person is Elder of age: " + str(age))


# if loop

age = 500
if age < 2:
    person = 'Baby'
if age < 4:
    person = 'Toddler'
if age < 13:
    person = ' Kid'
if age < 20:
    person = 'Teenager'
if age < 65:
    person = 'Adult'
if age > 65:
    person = 'Elder'

print(" The Person is " + person + ": " + str(age))

