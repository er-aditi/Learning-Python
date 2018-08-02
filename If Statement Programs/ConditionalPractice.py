# Tests for equality and inequality with strings
# name = 'aditi'
# print(name == 'aditi')
# if name == 'aditii':
#     print("It is correct")
#     name = 'jain'
# print(name == 'jain')

names = ["aaa", "bbb", "ccc", "dddd", "eeee", "ffff", "gggg", "hhhh", "iiii", "jjjj"]

for index in range(0, len(names)):
    print(str(index + 1) + ". " + names[index])

print("")
num = 0
for name in names:
    print(str(num + 1) + ". " + name)
    num += 1

