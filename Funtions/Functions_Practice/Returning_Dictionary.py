def formated_name(first_name, last_name):
    full_name = {'First_Name ': first_name, "Last_Name": last_name}
    return full_name


value = formated_name("Aditi", "Jain")
print(value["Last_Name"])