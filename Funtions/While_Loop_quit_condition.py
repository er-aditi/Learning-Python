def formated_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()


while True:
    print("Enter full detail")
    user = input("(If you want to quit then type 'q': )")
    if user == 'q':
        break
    f_name = input("First Name = ")
    l_name = input("Last Name = ")

    person = formated_name(f_name, l_name)
    print("Hello " + person + " !")

