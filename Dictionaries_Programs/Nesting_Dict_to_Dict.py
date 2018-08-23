users = {
    'eric': {
        'first': 'aditi',
        'last': 'jain',
        'location': 'gurugram'
    },
    'smith': {
        'first': 'Vine',
        'last': 'kumar',
        'location': 'delhi'
    }
}

for username, userinfo in users.items():
    print("\nUserName: " + username)
    FirstName = userinfo['first'] + ' ' + userinfo['last']
    Location = userinfo['location']

    print("\tFullName: " + FirstName)
    print("\tLocation: " + Location)

