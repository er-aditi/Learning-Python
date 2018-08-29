prompt = "Enter City Name: "
prompt += "\neither write 'quit: "

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print("I would like to go " + city)