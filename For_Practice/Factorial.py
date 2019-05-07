current_user = ['aditi', 'robb', 'stark', 'nedd']

new_users = ['aditi', 'thaons', 'thor', 'robb']

for new_user in new_users:
    if new_user in current_user:
        print(new_user + " Invited ")
    else:
        print(new_user + " Not Invited")
