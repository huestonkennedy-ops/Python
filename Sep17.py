import turtle
wn = turtle.Screen()
#create as many turtles as you want
t = turtle.Turtle()

#ADD CODE HERE

##setup

t.penup()
t.goto(-500, -100)
t.speed(0)

## draw the road and the grass underneath

t.pendown()
t.color("#808080", "#30C800")
t.pensize(30)
t.begin_fill()
for i in range(4):
    t.forward(1000)
    t.right(90)
t.end_fill()
t.pensize(1)
t.color("white")
for i in range(34):
    t.pendown()
    t.forward(20)
    t.penup()
    t.forward(10)

##making the blue sky and sun, using a loop to make rays

wn.bgcolor("#87CEEB")
t.penup()
t.goto(350, 300)
t.color("#FFE484", "#FFE484")
t.pensize(10)
t.pendown()
t.begin_fill()
t.circle(20)
t.end_fill()
for i in range(8):
    t.circle(20, 45)
    t.right(90)
    t.penup()
    t.forward(15)
    t.pendown()
    t.forward(20)
    t.right(180)
    t.penup()
    t.forward(35)
    t.right(90)

##making the wheels of the truck as a function

t.penup()
t.goto(-100, -85)
t.color("black", "black")
t.pensize(1)
def wheel(size, color="black", speed=0, ratio=2):
    t.pendown()
    t.speed(speed)
    t.color(color, color)
    t.begin_fill()
    t.circle(size)
    t.left(90)
    t.penup()
    t.forward(size/ratio)
    t.right(90)
    t.pendown()
    t.circle(size-(size/ratio))
    t.end_fill()
    t.color("white", "white")
    t.begin_fill()
    t.circle(size-size/ratio)
    t.end_fill()
    t.penup()
    t.right(90)
    t.forward(size-size/ratio)
    t.left(90)

##making a function for the main body of the truck

def body(size, ratio=3):
    t.pendown()
    t.color("black", "white")
    t.pensize(2)
    t.begin_fill()
    for i in range(2):
        t.forward(size)
        t.left(90)
        t.forward(size/ratio)
        t.left(90)
    t.end_fill()
    for i in range(3):
        t.pensize(1)
        t.left(90)
        t.color("black")
        t.forward(size/(ratio*4))
        t.right(90)
        t.color("#D3D3D3")
        t.forward(size)
        t.right(180)
        t.forward(size)
        t.right(180)
    t.penup()
    t.right(90)
    t.forward((3*size)/(ratio*4))
    t.left(90)
    t.forward(size)
\
## making a function for the front of the truck
def front(size, ratio=3):
    ##the main body
    t.pendown()
    t.color("black", "black")
    t.fd(size)
    t.begin_fill()
    t.left(90)
    t.fd(size/ratio)
    t.left(45)
    t.forward((size - (size/ratio))/0.7071067)
    t.left(45)
    t.fd(size/ratio)
    t.left(90)
    t.fd(size)
    t.end_fill()
    ##the glass pane
    t.penup()
    t.color("cyan", "cyan")
    t.left(90)
    t.forward(size/ratio)
    t.left(90)
    t.forward(size)
    t.pendown()
    t.begin_fill()
    t.left(180)
    t.forward(size - (size/ratio)-5)
    t.circle(5, 90)
    t.forward(size-(size/ratio))
    t.end_fill()

#building the truck, then turning it into a function

def truck(size):
    wheel(size*5)
    t.forward(size*50)
    wheel(size*5)
    t.penup()
    t.backward(size*50)
    t.left(90)
    t.forward(size*(30/4))
    t.right(90)
    t.bk(size*(25/4))
    body(size*(250/4))
    front(size*15)
    
##making a few trucks

t.penup()
t.bk(200)
truck(4)
t.penup()
t.fd(250)
t.right(90)
t.forward(60)
t.left(90)
truck(3)
#last line of code
wn.exitonclick()
