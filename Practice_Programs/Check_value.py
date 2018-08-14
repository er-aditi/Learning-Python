hardness = int(input("Enter Hardness of the steel "))
carbon = float(input("Enter carbon of the steel "))
tensile = int(input("Enter Tensile "))

h = hardness > 50
c = carbon < 0.7
t = tensile > 5600

if h and c & t:
    grade = 10
    print("Three conditions are met. Grade =  " + str(grade))

elif h & c:
    grade = 9
    print("conditions (h) and (c) are met. Grade =  " + str(grade))

elif c & t:
    grade = 8
    print("conditions (c) and (t) are met. Grade =  " + str(grade))

elif h & t:
    grade = 7
    print("conditions (h) and (t) are met. Grade =  " + str(grade))

elif h | c | t:
    grade = 6
    print("only one condition is met. Grade =  " + str(grade))

else:
    grade = 5
    print("None condition match. Grade =   " + str(grade))




