def city_country(city, country):
    fullname = '"' + city + ", " + country + '"'
    return fullname


var = city_country('goa', 'india')
print(var)