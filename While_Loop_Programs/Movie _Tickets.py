age = "Enter Age: "

# while True:
#     age_1 = input(age)
#     if int(age_1) < 3:
#         print("Ticket is Free")
#     elif int(age_1) < 12:
#         print("Ticket cost is 10")
#     else:
#         print("Ticket Cost is 15")


# Continue

while True:
    age_1 = input(age)
    if int(age_1) < 3:
        continue
    elif int(age_1) < 12:
        print("Ticket cost is 10")
    else:
        print("Ticket Cost is 15")