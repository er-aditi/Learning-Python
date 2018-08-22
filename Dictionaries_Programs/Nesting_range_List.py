aliens = []

for alien_num in range(30):
    new_alien = {'color': 'green', 'point': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[1:9]:
    print(alien)

print("\n-----")

print("Length of aliens: " + str(len(aliens)))
