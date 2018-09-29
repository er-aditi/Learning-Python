a = int(input("Enter 1st side: "))
b = int(input("Enter 2nd side: "))
c = int(input("Enter 3rd side: "))

if (a == b and c != a) or (b == c and a != b) or (c == a and b != a):
    print("Triangle is Isosceles ")
elif a == b == c:
    print("Triangle is Equilateral")
else:
    print("Triangle is scalene ")


