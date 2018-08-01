my_sets = set([1, 3])
print(my_sets)

my_sets.update([3, 4, 1, 2])
print(my_sets)

my_sets.add(9)
print(my_sets)

my_sets.update([2, 5], {3, 5})
print(my_sets)

my_sets.discard(5)
print(my_sets)


