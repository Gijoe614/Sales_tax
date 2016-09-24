cost = 1
totalCost = 0


print("Input prices. Enter 0 to indicate that you are done entering.")


while cost != 0:
    strCost = raw_input("Enter the cost of the item: ")

    cost = float(strCost)

    totalCost += cost
else:

    print ("The total is $" + str(totalCost))


strTax = raw_input("How much will you be taxed? Enter whole numbers, I will treat it as a percent: ")


sales_tax = float(strTax) / 100


total = totalCost * sales_tax
print("You will be taxed " + strTax + "%")

print("That is $" + str(round(total, 2)))
grandTotal = float(total) + totalCost

print("The total cost, with tax, is: $" + str(round(grandTotal, 2)))

