unconfirmed_users = ['alice', 'micky', 'vine']
confirmed_users = []

while unconfirmed_users:
    verify = unconfirmed_users.pop()

    print("Verify User: " + verify)
    confirmed_users.append(verify)

print("The Following users are confirmed: ")
for confirmed_user in confirmed_users:
    print(confirmed_user)