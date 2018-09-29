a = int(input("Enter 1st side "))
b = int(input("Enter 2nd side "))
c = int(input("Enter 3rd side "))

if a > b and a > c:
    x = b + c
    if a < x:
        print("It is valid Triangle")
    else:
        print("Invalid")
elif b > a and b > c:
    y = a + c
    if b < y:
        print("It is valid Triangle")
    else:
        print("Invalid")
elif c > a and c > b:
    z = a + b
    if c < z:
        print("It is valid Triangle")
    else:
        print("It is Invalid Triangle")





# if a < b:
#     if b > c:
#         print("b is grater " + str(b))
#     else:
#         print("c is greater " + str(c))
# else:
#     if a > c:
#         print("a is greater " + str(a))
#     else:
#         print("c is greater " + str(c))