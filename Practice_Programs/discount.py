quantity = input("Please enter the quantity ")
cost = input("Total amount ")
if int(quantity) > 1000:
    q = int(quantity) / 10
    cost = int(cost) - q
    print("Actual Price is after 10% discount:  " + str(cost))
else:
    print("Actual Cost: " + str(cost))


