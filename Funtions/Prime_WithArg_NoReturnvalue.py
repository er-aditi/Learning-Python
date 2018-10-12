def is_prime(num):
    var = 2
    while num > var:
        if num % var == 0:
            break
        var += 1
    if num == var:
        print(num, 'is Prime')


for index in range(1, 300):
    is_prime(index)