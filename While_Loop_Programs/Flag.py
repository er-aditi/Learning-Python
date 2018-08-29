prompt = "Enter any thing, I will Revert back to You!: "
prompt += "\nEither Enter 'quit: "


active = True

while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)


