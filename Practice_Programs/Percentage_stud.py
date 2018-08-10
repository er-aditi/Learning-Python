marks_maths = input("Marks in Maths = ")
print(int(marks_maths))
marks_science = input("Marks in Science = ")
print(int(marks_science))
marks_physics = input("Marks in Physics = ")
print(int(marks_physics))
marks_chem = input("Marks in Chem = ")
print(int(marks_maths))
marks_bio = input("Marks in Bio = ")
print(int(marks_bio))


total = (int(marks_maths)+int(marks_physics)+int(marks_science)+int(marks_bio)+int(marks_chem))/500
print(total)
percentage_1 = float(total)*100
print("Percentage = " + str(percentage_1) + "%")
