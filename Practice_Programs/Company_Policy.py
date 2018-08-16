order = int(input("Enter Order No.: "))
credit = input("Is Credit is OK? ")
stock = 50

if credit == 'Yes':
    if order <= stock:
        print("Supply Item ")
    else:
        items = order - stock
        print("Available Items are:" + str(stock) + ".\nNow, Remaining Items are " + str(items) + " shipped later.")

else:
    print("Not Supply")


