#Setting my constants
HST = 0.13
COST = 24.78
##Getting input from my user
length = float(input("Type in your length in metres: "))
width = float(input("Type in your width in metres: "))
##Calculating the perimetre, subtotal, tax, and total
perimetre = 2*(length+width)
subTotal = round(perimetre*COST, 2)
tax = round(subTotal*HST, 2)
total = round(subTotal + tax, 2)
##Displaying my results
print(length, "by", width, "metres will have a sub total of $", subTotal, ", a tax of $", tax, "and a total of $", total, "thanks!")