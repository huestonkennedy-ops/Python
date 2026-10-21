import math
import turtle
import random
wn = turtle.Screen()
#create as many turtles as you want
t = turtle.Turtle()
##getting my variables
xl = float(input("Select your lowest number on the x axis: "))
xh = float(input("Select your highest number on the x axis: "))
if xh<xl:
    print("Your max x value is less than your minimum x value! switching the values.\n")
    temp = xh
    xh = xl
    xl = temp
elif xh == xl:
    print("your maximum and minimum x values are the same! making your minumum x value 0.5 lower and  make x value 0.5 higher\n")
    xl -= 0.5
    xh += 0.5
yl = float(input("Select your lowest number on the y axis: "))
yh = float(input("Select your highest number on the y axis: "))
if yh<yl:
    print("Your max y value is less than your minimum y value! switching the values.\n")
    temp = yh
    yh = yl
    yl = temp
elif yh == yl:
    print("your maximum and minimum y values are the same! making your minumum y value 0.5 lower and  make y value 0.5 higher\n")
    yl -= 0.5
    yh += 0.5
xf = float(input("Select the frequency of the markers on the x axis: "))
yf = float(input("Select the frequency of the markers on the y axis: "))
print(xh)
print(xl)
xrange = (xh - xl)
yrange = (yh - yl)
xspacing = ((xf*860)/xrange)
yspacing = ((yf*860)/yrange)
##drawing my x axis
t.pu()
t.pensize(4)
t.goto(-430, 0)
t.pd()
t.right(45)
t.fd(20)
t.bk(20)
t.left(90)
t.fd(20)
t.bk(20)
t.right(45)
x = -430
xvalue = xl
t.seth(0)
t.speed(0)
while x<430:
    if (x+xspacing)<430:
        t.fd(xspacing)
        x += xspacing
        xvalue += xf
        if x<430:
            t.left(90)
            t.fd(15)
            t.write(round(xvalue, 3))
            t.bk(30)
            t.fd(15)
            t.pensize(0.5)
            t.fd(700)
            t.bk(1400)
            t.fd(700)
            t.right(90)
            t.pensize(4)
    else:
        x += xspacing
        t.goto(430, 0)
t.left(135)
t.fd(20)
t.bk(20)
t.left(90)
t.fd(20)
##drawing my y axis
t.pu()
t.goto(0, -430)
t.pd()
t.seth(135)
t.fd(20)
t.bk(20)
t.right(90)
t.fd(20)
t.bk(20)
t.left(90)
t.right(45)
y = -430
yvalue = yl
while y<430:
    if (y+yspacing)<430:
        t.fd(yspacing)
        y += yspacing
        yvalue += yf
        if y<430:
            t.right(90)
            t.fd(15)
            t.write(round(yvalue, 3))
            t.bk(30)
            t.fd(15)
            t.pensize(0.5)
            
            t.fd(700)
            t.bk(1400)
            t.fd(700)
            t.left(90)
            t.pensize(4)
    else:
        y += yspacing
        t.goto(0, 430)
t.left(135)
t.fd(20)
t.bk(20)
t.left(90)
t.fd(20)
##graphing the function
done = False
##Making it keep asking you for input until you type one of the working functions, so users won't have to redo it
while done == False:
    type = input("Select your type of equation, 'linear', 'polynomial', 'exponential', 'logarithmic', 'sinusoidal', 'parametric', or 'polar': ")
    if type=="linear":
        strings = list(input("Type your linear equation, format 'y = mx + b': "))
        number = 0
        mybool = True
        coeftemp = ''
        ##identifying the coefficient
        
        while mybool==True:
            num = strings[number]
            if num == 'y':
                pass
            elif num == ' ':
                pass
            elif num == '-':
                coeftemp += num
            elif num == '=':
                pass
            elif num == 'x':
                mybool = False
            else:
                coeftemp += num
            number += 1
        if coeftemp == '':
            coefficient = 1
        elif coeftemp == '-':
            coefficient = -1
        else:
            coefficient = float(coeftemp)
        ##identifiying the constant
        consttemp = False
        consttemp = ''
        spaces = 0
        while number<len(strings):
            num = strings[number]
            if num == 'x':
                pass
            elif num == '-':
                consttemp += num
            elif num == '+':
                pass
            elif num == ' ':
                pass
            else:
                consttemp += num
            number += 1
        #adding zero to the end of consttemp to deal with when users don't type a constant, for example y = 5x. I will then divide by ten to restore the original numbers
        ##I made it take the integer twice to deal with python changing it to a double with division
        consttemp += '0'
        constant = ((float(consttemp)/10))
        ##calculating the start values and end values of the function 
        def f(x):
            return x*coefficient + constant
        ystart = f(xl)
        ##drawing the function
        
        t.pu()
        t.color("red")
        ymid = (yl+yh)/2
        ystart = f(xl)
        print(ystart)
        ydistance = ystart - ymid
        ycord = (430*ydistance)/(yrange/2)
        t.goto(-430, ycord)
        angle = (math.atan(coefficient*(xrange/yrange)))*(180/3.1415926589897)
        print(angle)
        t.seth(angle)
        t.pd()
        t.fd(10000)
        t.bk(20000)
        t.pu()
        print(ystart)
        done = True
    elif type == "polynomial":
        strings = list(input("Type in your function, format y = ax^b + cx^d... + n: "))
        ##Identifying how many non constant terms the function has
        number = 0
        terms = 1
        hasConstant = False
        consttemp = ''
        while number<len(strings):
            if strings[number] == 'x':
               terms += 1
            number += 1
        number -= 1
        found = False
        ##Identifying the constant
        while found == False:
            if strings[number] == 'x':
                found = True
            elif strings[number] == '+':
                found = True
                constant = True
            elif strings[number] == ' ':
                pass
            else:
                consttemp += strings[number]
            number -= 1
        if hasConstant == True:
            constant = float(consttemp)
        else:
            constant = 0
        number = 0
        coefNumber = 0
        ##Identifying each coefficient and exponent
        exponents = []
        coefficients = {}
        found = False
        while found == False and number < len(strings):
            if strings[number] == 'x':
                found = True
            number -= 1
        found = False
        while found == False:
            if number<0:
                found = True
                number += 1
            elif strings[number] == '=':
                found = True
                number += 1
            elif strings[number] == ' ':
                found = True
                number += 1
            elif strings[number] == '-':
                found = True
                number += 1
            else: number -= 1
        done = True
    else:
        print("Sorry, there was an error. Make sure you spelled it correctly or try a different function. \n \n the only functions currently working are: linear")
wn.exitonclick()