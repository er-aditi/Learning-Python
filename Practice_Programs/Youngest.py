ram = int(input("Enter Age of Ram "))
shyam = int(input("Enter Age of Shyam "))
ajay = int(input("Enter Age of Ajay "))

if ram < shyam:
    if ram > ajay:
        print("Ajay is Younger")
    else:
        print("Ram is Younger")
else:
    if shyam > ajay:
        print("Ajay is younger")
    else:
        print("shyam is younger")


