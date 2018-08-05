alien_color = 'pink'
if alien_color == 'green':
    print("player earned 5 points.")
elif alien_color == 'yellow':
    print("player earned 10 points.")
elif alien_color == 'red':
    print("player earned 15 points.")


# In single print

alien_color = 'green'
if alien_color == 'green':
    point = 5
elif alien_color == 'yellow':
    point = 10
elif alien_color == 'red':
    point = 15

print("Alien Color is: " + alien_color + "\n " + str(point))
