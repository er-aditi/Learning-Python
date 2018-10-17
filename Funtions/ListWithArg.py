records = [5, 6, 8, 88, 1]


def find_largest(data):
    var = 1
    high = data[0]
    # for var in range(1, len(str(data))+1):
    while var < len(data)-1:
        if high < data[var]:
            high = data[var]
            var += 1

    print(high, "is the highest number")


find_largest(records)
