num = int(input("Enter Range: "))


def fibonaci(var):
    num_1 = 1
    num_2 = 0
    count = 0
    store = [0, 1]
    # print(num_2, num_1, end=" ")
    while count < var:
        value = num_1 + num_2

        num_2 = num_1
        num_1 = value

        count += 1

        store.append(value)
    return store


value1 = fibonaci(num)
print(value1)

