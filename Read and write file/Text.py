fw = open("Simple.txt", 'w')
fw.write("Hi writing some text\n")
fw.write("It's pretty easy")
fw.close()


fr = open("Simple.txt", 'r')
text = fr.read()
print(text)
fr.close()