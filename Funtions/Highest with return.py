def create_list():
    users = int(input("Enter Limit: "))
    store = list()
    for user in range(1, users+1):
        value = int(input("enter number: "))
        store.append(value)

    print(store)
    find_largest(store)


def find_largest(data):
    var = 1
    high = data[0]
    # for var in range(1, len(str(data))+1):
    while var < len(data)-1:
        if high < data[var]:
            high = data[var]
            var += 1

    print(high, "is Largest Number ")


create_list()
