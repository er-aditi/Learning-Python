menus = ('panner', 'dal', 'mix veg', 'soy chaap')
for menu in menus:
    print(menu.title())

# # menus[1] = 'dosa'
# # print(menus)
# print("\n--------------------------\n")
#
# # reviced_menus = ('idly', 'dosa')
# #
# # for menu in reviced_menus:
# #     print(reviced_menus)

lst = list(menus)
lst[0] = 'idly'
lst[1] = 'dosa'
print(tuple(lst))
for lst1 in lst:
    print(lst1.title())
