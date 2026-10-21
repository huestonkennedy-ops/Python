#gathering my information
mathGrade = float(input("Math grade? "))
englishGrade = float(input("English grade? "))
csGrade = float(input("Computer science grade? "))
school = input("What school do they go to? ")
city = input("What city is it in? ")
province = input("What province? ")
firstName = input("First name? ")
lastName = input("Last name? ")
classAverage = float(input("What is the class average? "))
#calculating the average and distance from average
studentAverage = round((csGrade+mathGrade+englishGrade)/3, 2)
if studentAverage<classAverage:
    belowAverage = True
else:
    belowAverage = False
distFromAvg = abs(studentAverage - classAverage)
##Printing the results
print("\t Student Report")
print(" \t   " + school)
print("Student name: " + firstName + " " + lastName)
print("\nCurrent marks for " + firstName +" are:")
print("\nMath:\t", mathGrade, "\nEnglish: \t", englishGrade, "\nCS:\t", csGrade, "\n" )
print("Overall average for", firstName, lastName, "is:", studentAverage, "%")
print("\n", firstName, lastName, "is", distFromAvg, "% away from class average of", classAverage, "%\n")
print("All student reports are to be returned to: " + school)
print("\n City/Province: " + city + "-" + province)