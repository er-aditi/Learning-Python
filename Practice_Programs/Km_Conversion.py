# m=km*1000
# cm=m*100
# feet=km*3280.8
# inch=feet*12

distance_km = input("Please Enter distance of 2 Cities: ")
print("Distance in Km: " + str(distance_km))
meter = int(distance_km)*1000
cm = int(meter)*100
feet = int(distance_km)*float(3280.8)
inch = float(feet)*12
print("Meter = " + str(meter))
print("Centimeter = " + str(cm))
print("Feet = " + str(feet))
print("Inch = " + str(inch))


