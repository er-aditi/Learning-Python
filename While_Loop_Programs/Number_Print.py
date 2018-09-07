# num = 1
# val = 11
# while num <= 9:
#     print(num)
#     var = 1
#     while var <= 10:
#         print("\t---------" + str(val))
#         var += 1
#         val += 1
#     num += 1


num = 1
while num <= 9:
    print(num)
    var = 1
    while var <= 10:
        print("\t--------- " + str((num * 10) + var))
        var += 1
    num += 1