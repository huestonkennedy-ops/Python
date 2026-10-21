##setting my constants
HST = 0.13
HMCOST = 4.95
BBBCOST = 5.35
BYBCOST = 3.25
##asking how many of each item the customer wants
hmQuant =int(input("How many Hangry Meals would you like?" ))
bbbQuant = int(input("How many Bacon, Bacon, and Bacon sandwiches would you like?" ))
bybQuant = int(input("How many Big Yum Burgers would you like? "))
##cheking to see if the quantities make sense
if hmQuant < 0 or bbbQuant < 0 or bybQuant < 0:
    print("You can't order negative items!")
elif hmQuant > 10 or bbbQuant > 10 or bybQuant > 10:
    print("We are out of stock of one or more of your chosen items")
else:
    ##calculating the total prices of each item
    hmCharge = HMCOST*hmQuant
    bbbCharge = BBBCOST*bbbQuant
    bybCharge = BYBCOST*bybQuant
    ##calculating the tax and total
    subTotal = hmCharge + bbbCharge + bybCharge
    tax = round(subTotal*HST, 2)
    ##also rounding total because sometimes python has errors when adding floats
    total = round(tax + subTotal, 2)
    ##printing the receipt
    print("\n")
    print("Hangry Meal x", hmQuant, "total: $", hmCharge)
    print("Bacon, Bacon, Bacon Sandwich x", bbbQuant, "total: $", bbbCharge)
    print("Big Yum Burger x", bybQuant, "total: $", bybCharge)
    print("subtotal: $", subTotal)
    print("HST: $", tax)
    print("total: $", total)

    ##asking for tips after the receipt has been printed so they know how much they are tipping
    tip = (int(input("Please enter your tip percentage")))/100
    tipCost = round(tip*total, 2)
    ##Telling them how much money that tip would be
    print("/n")
    print("That tip would cost $", tipCost, "are you sure you want to tip?")
    ##checking to see if they still want to tip 
    tipping = input("Type 1 if you would still like to tip, 2 if you do not want to tip, and 3 if you want to enter a new tip")
    if tipping == '1':
        pass
    elif tipping == '2':
        tip = 0
        tipCost = 0
    elif tipping == '3':
        tip = (int(input("Select your tipping percentage. This will be final")))/100
        tipCost = round(tip*total, 2)
        print("That tip will cost $", tipCost, "thanks!")
    ##printing what their new total is
    newTotal = round(tip + total, 2)
    print("\n \nYour new total is now $", newTotal, "thanks!")