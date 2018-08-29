toppings = "Enter Pizza Toppings: "
toppings += "\nEither Enter 'quit': "

# message = ""
# while message != 'quit':
#     message = input(toppings)
#     print(message)

# while True:
#     message = input(toppings)
#     if message == 'quit':
#         break
#     else:
#         print(message)

active = True
while active:
    message = input(toppings)
    if message == 'quit':
        active = False
    else:
        print("User Like to add: " + message)