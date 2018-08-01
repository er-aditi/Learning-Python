mountains = ['Kangchenjunga', 'Nanda Devi', 'Kamet', 'Saltoro Kangri']
rivers = ['ganga', 'yamuna', 'gumti', 'surma']
countries = ['india', 'pakistan', 'US', 'euro']
cities = ['goa', 'delhi', 'bhind', 'gwalior']
store = ['mobile', 'cloths', 'footwear', 'jewelery']

print("Length of Mountain: ", len(mountains), mountains)
mountains.sort()
print(mountains)
print(store)
print(rivers)
print(cities)
print(countries)
countries.sort(reverse=True)
countries.append('sri lanka')
print(countries)
del cities[2]
print(cities)

cities.remove('goa')
print(cities)

list_4 = store.pop(1)
print(list_4)
print(store)

cities[1] = 'pune'
print(cities)

cities.insert(1, 'jaipur')
print(cities)

countries.sort(reverse=True)
print(countries[0].title(), len(countries))
print(countries)

