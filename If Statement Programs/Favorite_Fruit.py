fruits = ['apple', 'banana', 'jelly', 'mango', 'blueberry']
if 'apple' in fruits:
    print(" I Like Apples")

data = 'berry'
if data in fruits:
    print("It my fav. " + data)

if 'blueberry' in fruits:
    print("Its my fav")

is_condition = False
for fruit in fruits:
    if fruit == 'berry':
        is_condition = True

if is_condition:
    print("I Like it")
for index in range(0, len(fruits)):
    print(str(index+1) + ". " + fruits[index])