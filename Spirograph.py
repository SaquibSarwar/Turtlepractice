#Python Turtle - Spirograph - www.101computing.net/python-turtle-spirograph/
import turtle
from math import cos,sin
from time import sleep
import random
# http://www.101computing.net/python-turtle-spirograph/
window = turtle.Screen()
turtle.speed(0)
window.bgcolor("#FFFFFF")
m = turtle.Turtle()
R = 90
r = 97
d = 80
#c=e=random.randrange()
angle = 0
theta = 0.2
steps = int(100*3.14/theta)
#for
for t in range(0,steps):
  angle += theta
  x = (R - r) * cos(angle) - random.randint(1,3)*d * cos(((R-r)/r)*angle)
  y = (R - r) * sin(angle) - random.randint(3,5)*d * sin(((R-r)/r)*angle)
  m.goto(x,y)
turtle.done()
#homework implement other formulas
#make it random and crazy
