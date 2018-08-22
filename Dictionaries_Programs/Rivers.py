rivers = {
    'nile': 'egypt',
    'Drava': 'austria',
    'Bakoy': 'Guinea',
    'Imjin': 'Korea',
    'Salinas': 'mexico'
    }

for river, country in rivers.items():
    print("The " + river.title() + " runs through " + country.title() + ".")

print("\nRivers\n----------------------------")
for river in rivers.keys():
    print(river.title())

print("\nCountry\n----------------------------")
for country in rivers.values():
    print(country.title())