favorite_languages = {
    'vine': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
members = ['vine', 'aditi', 'sarah', 'phil']

for member in members:
    # print(member)

    if member in favorite_languages.keys():
        print("Thanking " + member.title() + " for responding. Language is: ".title() + favorite_languages[member])
    else:
        print("Inviting " + member.title() + " to take the poll.")




