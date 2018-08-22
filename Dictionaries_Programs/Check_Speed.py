alien = {'x_position': 0, 'y_position': 25, 'color': 'green', 'speed': 'medium'}

print("Original X-Position: " + str(alien['x_position']))

if alien['speed'] == 'slow':
    x_increment = 1

elif alien['speed'] == 'medium':
    x_increment = 2

else:
    x_increment = 3

final_value = alien['x_position'] + x_increment

print("Final Position " + str(final_value))
