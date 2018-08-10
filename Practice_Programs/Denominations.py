money = int(input("Please Enter amount multiple of 100: "))
note_100 = money//100
rem_1 = money % 100
note_50 = rem_1 // 50
rem_2 = rem_1 % 50
note_10 = rem_2 // 10
print("Note of 100 " + str(note_100))
print("Note of 50  " + str(note_50))
print("Note of 10: " + str(note_10))
