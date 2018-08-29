fav_numbers = {
    'alien': [8, 4],
    'john': [9, 66],
    "tom": [5, 8],
    'smith': [33, 88],
    'dis': [55, 88]
}
for name, numbers in fav_numbers.items():
    print(name.title() + "' Fav Number are: ")

    for number in numbers:
        print("\t" + str(number))
