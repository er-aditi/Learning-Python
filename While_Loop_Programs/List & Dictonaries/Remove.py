sandwich_orders = ['onion', 'mix', 'cucumber', 'tomato', 'potato', 'onion', 'onion']
finished_sandwiches = []
print(sandwich_orders)
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print("I like to have " + sandwich.title() + " Sandwich")

    finished_sandwiches.append(sandwich)

while 'onion' in finished_sandwiches:
    finished_sandwiches.remove('onion')

print("\nNow onion Sandwiches are Finished-----\n ")
print(finished_sandwiches)
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title() + " Sandwich is Available")
