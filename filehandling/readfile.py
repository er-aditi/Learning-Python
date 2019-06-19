read_file = open("textfile.txt", 'r')

print(str(read_file.read()))
read_file.close()
print("Read file line by line --------------------")

read_file_line = open('textfile.txt', 'r')

print(str(read_file_line.readline()))
print(str(read_file_line.readline()))
read_file_line.close()