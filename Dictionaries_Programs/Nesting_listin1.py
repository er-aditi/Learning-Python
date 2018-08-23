fav_language = {
    'jen': ['ruby', 'C'],
    'tom': ['python', 'c'],
    'harry': ['java']
}

for name, langs in fav_language.items():
    print("\n" + str(name.title()) + " Fav. Language is: ")
    for lang in langs:
        print("\t" + str(lang))