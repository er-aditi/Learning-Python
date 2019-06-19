# """"with as keyword'''
# my_file = open("write.txt", 'w')
#
# my_file.write("This is written file")
# my_file.close()
#
# my_file_read = open("write.txt", 'r')
# print(str(my_file_read.read()))
# my_file.close()


with open("withas.txt", 'w') as with_as_write:
    with_as_write.write("Checking with as keyword")

print()
print("checking read")

with open("withas.txt", 'r') as with_as_read:
    print(str(with_as_read.read()))