def lets_make_pizza(*toppings):
    print("\nMake a different Toppings List: ")
    for topping in toppings:
        print("- ", topping)


lets_make_pizza("Mushroom")
lets_make_pizza("Onion", 'olive', 'corn')


