cost_price = int(input("Enter cost Price "))
selling_price = int(input("Enter Selling Price "))
if cost_price < selling_price:
    profit = selling_price-cost_price
    print("Profit amount is: " + str(profit))
else:
    loss = cost_price-selling_price
    print("Loss amount is : " + str(loss))
