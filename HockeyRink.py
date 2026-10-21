#Setting the constant cost per litre
COST =  0.0042
#Asking the user for the dimensions fo the rink.
length = float(input("What is the length in metres? "))
width = float(input("What is the width in metres? "))
thickness = float(input("What is your desired thickness in metres? "))
##Calculating the volume and cost
volumeMetres = length*width*thickness
volumeLitres = volumeMetres*1000
totalCost = round(volumeLitres*COST, 2)
##Displaying the results
print(volumeLitres, "litres of ice will cost a total of $", totalCost)