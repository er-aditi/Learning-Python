my_list = [1, 2, 3]

my_file = open("textfile.txt", 'w')

for index in my_list:
    my_file.write(str(index)+ "\n")

my_file.close()