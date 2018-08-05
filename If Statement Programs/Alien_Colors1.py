alien_color = ['green', 'yellow', 'red']
if 'green' in alien_color:
    print("He Earned 5 points")
if 'white' in alien_color:
    print("Wonderfull")

is_green_available = False

for alen in alien_color:
    if alen == 'green':
        is_green_available = True

if is_green_available:
    print("Avaiable")
else:
    print("Not Found")


