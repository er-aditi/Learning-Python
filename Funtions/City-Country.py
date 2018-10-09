def city_country(city, country):
    full = city + ', ' + country
    return full.title()


num = 1
while num <= 3:
    f_name = input("City = ")
    l_name = input("Country = ")
    num += 1

    print('" ' + city_country(f_name, l_name) + ' "')

