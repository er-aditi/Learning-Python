my_set1 = {1, 3, 5, 9, 55}
my_set2 = {1, 2, 9, 7, 8}

# union
allsets = my_set1 | my_set2
print(allsets)

# intersection
allsets = my_set1 & my_set2
print(allsets)

# set difference
allsets = my_set1 - my_set2
print(allsets)

# Set Symmetric Difference
allsets = my_set1 ^ my_set2
print(allsets)
print("\n -----------------\n")

allsets = my_set2 - my_set1
print(allsets)


