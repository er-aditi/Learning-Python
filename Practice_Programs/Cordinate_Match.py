x1 = int(input("Enter Value of x1 "))
y1 = int(input("Enter Value of y1 "))
x2 = int(input("Enter Value of x2 "))
y2 = int(input("Enter Value of y2 "))
x3 = int(input("Enter Value of x3 "))
y3 = int(input("Enter Value of y3 "))

if x1 == x2 == x3:
    print("These point lies in single line of x coordinate ")
elif y1 == y2 == y3:
    print("These point lies in single line of y coordinate ")
else:
    print("Points are not on same line ")