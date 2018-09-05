num = "Enter number to find out Negative, Positive, 0 Number: "
new = "-----------------Do you wants to more enter:?  "
positive = 0
negative = 0
zero = 0
count = 0
while True:
    user = int(input(num))
    count = count + 1
    if 0 < user:
        positive = positive + 1
    elif user == 0:
        zero = zero + 1
    else:
        negative = negative + 1
    cond = input(new)
    if cond == 'No':
        break
print("\nResult is -----------")
print("Count is: " + str(count))
print("Positive Numbers are: " + str(positive))
print("Negative Numbers are: " + str(negative))
print("Zero Numbers are: " + str(zero))