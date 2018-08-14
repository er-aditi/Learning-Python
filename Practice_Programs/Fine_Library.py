days = int(input("enter number of days for fine "))

if days < 5:
    print("Fine is 50 paise ")

elif days < 10:
    print("Fine is 1 rupee ")

elif days < 30:
    print("Fine is 5 rupees ")
else:
    print("Your membership will be cancelled")
