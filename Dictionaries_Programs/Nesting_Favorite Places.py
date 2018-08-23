favorite_places = {
    'aditi': ['goa', 'paris'],
    'vine': ['london', 'france'],
    'manya': ['gurugram', 'delhi']
    }

for name, places in favorite_places.items():
    print("\nName: " + name.title())
    for place in places:
        print("\tPlace: " + place.title())