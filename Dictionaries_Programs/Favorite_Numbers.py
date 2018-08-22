fav_numbers = {'alien': 8, 'john': 9, "tom": 5, 'smith': 33, 'dis': 88}
print(fav_numbers)

print("alien fav no is ".title() + str(fav_numbers['alien']))
print("john fav no is ".title() + str(fav_numbers['john']))
print("tom fav no is ".title() + str(fav_numbers['tom']))
print("smith fav no is ".title() + str(fav_numbers['smith']))
print("dis fav no is ".title() + str(fav_numbers['dis']))

fav_numbers['Vineet'] = 89

print(fav_numbers)

fav_numbers['john'] = 95
print("John " + str(fav_numbers['john']))