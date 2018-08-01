names = ['aleen', 'john', 'tom']
message = ", You are invited for dinner!"
names.insert(0, 'aditi')
names.insert(2, 'vine')
names.append('berry')
print(names[0] + message)
print(names[1] + message)
print(names[2] + message)
print(names[3] + message)
print(names[4] + message)
print(names[5] + message)

print("\n you can invite only two people for dinner. \n ")
name = names.pop(1)
print(name.title() + ", Sorry for the dinner")
name = names.pop(2)
print(name + ", Sorry for dinner ")
name = names.pop(3)
print(name + ", Sorry for dinner")
name = names.pop(2)
print(name + ", sorry for dinner")
print(names)
print("\n -------------------------\n")

print(names[0] + " You are most welcome")
print(names[1] + " you are most welcome")

del names[0]
del names[0]
print(names)