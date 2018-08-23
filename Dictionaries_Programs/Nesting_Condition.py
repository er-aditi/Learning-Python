aliens = []

for alien_num in range(20):
    new_alien = {'color': 'green', 'speed': 'slow', 'point': 5}
    aliens.append(new_alien)

for alien in aliens[:3]:
    # if alien['color'] == 'green':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['point'] = 55

for alien in aliens[:5]:
    print(alien)

print("\n-----------")



