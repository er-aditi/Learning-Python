def is_prime(num):
    var = 2
    while num > var:
        if num % var == 0:
            break
        var += 1
    if num == var:
        return True
    else:
        return False


for index in range(1, 300):
    if is_prime(index):
        print(index, "is Prime")










