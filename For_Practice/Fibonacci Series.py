t1 = 0
t2 = 1
print(t1, t2, end=" ")
for num in range(0, 10):
    t3 = t2 + t1

    print(t3, end=" ")
    t1 = t2
    t2 = t3