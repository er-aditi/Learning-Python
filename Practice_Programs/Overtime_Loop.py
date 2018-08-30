hour = "Enter extra hour: "
emp = 1
while emp <= 10:
    time = input(hour)
    if int(time) > 40:
        total = int(time) - 40
        cal = total * 12
        print("Extra work hour, Amount to be paid: " + str(cal))
    else:
        print("Not work for extra four")

    emp += 1

