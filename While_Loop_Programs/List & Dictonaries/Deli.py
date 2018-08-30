sandwich_orders = ['mix', 'cucumber', 'tomato', 'potato',  'onion']
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print("I like to have " + sandwich.title() + " Sandwich")

    finished_sandwiches.append(sandwich)


print("\nFinished Sandwiches are---\n")
for finished_sandwiche in finished_sandwiches:
        print(finished_sandwiche.title() + " are finished")
