data = ['file', 'Doc', 'Folder', 'download']
poped_message = data.pop()
message = 'I wants to store my data in '

print(message + poped_message.title() + '.')
print(data[-1])

data.append('paint')
print(data)

del data[3]
print(data)

data.insert(1, 'SQL')
print(data)