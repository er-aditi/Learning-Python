length = int(input("Enter The length of Rectangle "))
breadth = int(input("Enter Breadth of Rectangle "))
area = length * breadth
print("Area = " + str(area))
perimeter = 2*(length+breadth)
print("Perimeter = " + str(perimeter))
if area > perimeter:
    print("Area is greater than perimeter ")
else:
    print("Area is smaller than Perimeter")