pizzas = ['onion', 'corn', 'panner']
friend_pizzas = pizzas[:]

print("My fav pizzas are: " + "\n" + str(pizzas))
print("\n" + "My Friends Fav Pizza are: " + "\n" + str(friend_pizzas))

pizzas.append('capsiccum')
friend_pizzas.append('tomato')

print("\n -----------------------------------------------\n")
print("My fav Pizzas Are: ")
for pizza in pizzas:
    print(pizza)

my_pizzas = list(pizzas)
print(my_pizzas)

print("\n" + "My Friends fav Pizzas Are: ")

for friend_pizza in friend_pizzas:
    print(friend_pizza)

myfriend_pizzas = list(friend_pizzas)
print(myfriend_pizzas)