current_users = ['smith', 'aleen', 'tom', 'aditi', 'JOHN']
new_users = ['berry', 'bim', 'tom', 'john']

for new_user in new_users:
    if new_user in current_users:
        print("This user is already exits " + new_user + ".")
    else:
        print("Username is available " + new_user + ".")

