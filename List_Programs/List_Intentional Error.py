cities = ['goa', 'manali', 'shimla', 'delhi']
daily = ['tea', 'roti', 'sabji']

print(cities[0].title())
print(cities[-1].upper())

print(cities.remove('goa'), cities)
print(cities.copy())
daily.extend('Aditi')
print(daily, len(daily))