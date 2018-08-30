responses = {}
active = True
while active:
    name = input("Enter Your Name: ")
    response = input("Which place would you like to go: ")

    responses[name] = response

    repeat = input("Again Want? ")
    if repeat == 'No':
        active = False

print("---Poll End------")

for name, response in responses.items():
    print(name + " Like's to Go " + response)