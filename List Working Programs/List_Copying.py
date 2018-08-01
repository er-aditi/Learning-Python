# List Copying with[:]

my_foods = ['pizza', 'pasta', 'dosa']
friends_food = my_foods[:]

print("My Fav. Foods Are : " + "\n" + str(my_foods) + "\n")
print("My Friends Fav Foods are: " + "\n" + str(friends_food))

my_foods.append('ice_cream')
friends_food.append('coke')
print("\n" + "------------------------------------------------------" + "\n")

print("\n" + "My Fav. Foods Are : " + "\n" + str(my_foods) + "\n")
print("My Friends Fav Foods are: " + "\n" + str(friends_food))

# List Copying without[:]
print("\n***************************************************")
print("List Copying without[:]")
my_foods = ['pizza', 'pasta', 'dosa']
friends_food = my_foods

print("\n" + "My Fav. Foods Are : " + "\n" + str(my_foods) + "\n")
print("My Friends Fav Foods are: " + "\n" + str(friends_food))

my_foods.append('ice_cream')
friends_food.append('coke')
print("\n" + "------------------------------------------------------" + "\n")

print("\n" + "My Fav. Foods Are : " + "\n" + str(my_foods) + "\n")
print("My Friends Fav Foods are: " + "\n" + str(friends_food))
