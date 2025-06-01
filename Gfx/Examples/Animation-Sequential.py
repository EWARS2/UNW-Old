from vpython import *
import math

# Objects
myText1 = text(pos = vector(10,0,0),text='X axis', height = 0.3)
myText2 = text(pos = vector(0,10,0),text='Y axis', height = 0.3)
myText3 = text(pos = vector(0,0,10),text='Z axis', height = 0.3)
myArrow1 = arrow (pos = vector (0,0,0), axis=vector(1,0,0),color = color.red, length = 10, shaftwidth = 0.2)
myArrow2 = arrow (pos = vector (0,0,0), axis=vector(0,1,0),color = color.red, length = 10, shaftwidth = 0.2)
myArrow3 = arrow (pos = vector (0,0,0), axis=vector(0,0,1),color = color.red, length = 10, shaftwidth = 0.2)

#Animation
xPos = yPos = zPos = -2
mySphere2 = sphere(make_trail=True, pos=vector(xPos, yPos, zPos), color=vector(0.5, 0.5, 0.5), radius = 0.2)
for i in range(10):
    dx = -0.1
    dy = math.cos(i)
    dz = math.sin(i)
    xPos += dx
    yPos += dy
    zPos += dz
    mySphere2.pos=(vector(xPos,yPos,zPos))
    sleep(1)