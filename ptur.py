import turtle

import random
turtle.screensize(canvwidth=600, canvheight=600, bg=None)

t= turtle.Turtle()
#wn = turtle.Screen()

t.home()
t.speed(0)
x= int(input('Line Length: '))
y= int(input('Line circle redious: '))
z= int(input('Give circle angle: '))
i=0
J=0
while i<1000:

    t.fd(x+J)
    t.circle(y,z)
    i=i+1
    if i==200: J=x
    
    coin = random.randrange(0, 2)
    if coin == 0:              # heads
        t.left(90)
    else:                      # tails
        t.right(90)



#print (t.position())
