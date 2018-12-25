def formatted_name(First_name, Last_Name, Middle_Name = ""):
    if Middle_Name:
        full_name = First_name + " " + Middle_Name + " " + Last_Name
    else:
        full_name = First_name + " " + Last_Name
    return full_name


value = formatted_name('Aditi', 'jain')
print(value)

value = formatted_name("Vine", "Kumar", 'si')
print(value)



