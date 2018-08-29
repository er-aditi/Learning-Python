prompt = "Please Enter Something"
prompt += "\n You can enter 'quit'"

message = " "
while message != 'quit':
    message = (input(prompt))

    if message != 'quit':
        print(message)
