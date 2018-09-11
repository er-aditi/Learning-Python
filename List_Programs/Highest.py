num = 1

data = [8, 9, 5, 1, 77, 6]

high = data[0]
while num <= len(data)-1:
    if high < data[num]:
        high = data[num]

    num += 1

print("Highest: " + str(high))




