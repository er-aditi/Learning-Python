cities = {
    'goa': {
        'country': 'india',
        'population': '500000',
        'fact': 'for Beaches'
     },
    'manali': {
        'country': 'india',
        'population': '400000',
        'fact': 'for Hills'
    }
}

for city, city_info in cities.items():
    print("City name is: " + city + "'s Info are: ")
    country = city_info['country']
    population = city_info['population']
    facts = city_info['fact']

    print('\tCountry: ' + country)
    print("\tpopulation: " + population)
    print("\tfacts: " + facts)
