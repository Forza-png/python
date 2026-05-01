actual_cost = float(input("Enter the actual cost: "))
selling_price = float(input("Enter the selling price: "))

if selling_price > actual_cost:
    amount = selling_price - actual_cost
    print("Total Profit = {0}".format(amount))

else:
    print("No profit, no loss.")
