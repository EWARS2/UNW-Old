from vpython import *
import math
# Objects
myText = text(pos = vector(10,0,0),text='X axis', height = 0.3)
myText = text(pos = vector(0,10,0),text='Y axis', height = 0.3)
myText = text(pos = vector(0,0,10),text='Z axis', height = 0.3)
myArrow1 = arrow (pos = vector (0,0,0), axis=vector(1,0,0),color = color.red, length = 10, shaftwidth = 0.2)
myArrow2 = arrow (pos = vector (0,0,0), axis=vector(0,1,0),color = color.red, length = 10, shaftwidth = 0.2)
myArrow3 = arrow (pos = vector (0,0,0), axis=vector(0,0,1),color = color.red, length = 10, shaftwidth = 0.2)
mySphere = sphere(pos = vector(5,5,5), color = vector(0.5,0.5,0.5))
myBox1 = box(pos = vector(-3,0,0), color = color.green, size=vector(0.5,1.0,1.0))
myCylinder0 = cylinder(pos = vector(0,5,0), color = color.blue,length = 3, radius = 0.5)
myPyramid1 = pyramid (pos = vector(3,1,0), color = color.green, length = 0.5, width = 1.0, height = 1.0)
myCone = cone(pos=vector(5,2,0), axis=vector(4,0,0), radius=1)
myCurve = curve(vector(-1,-1,0), vector(1,-1,0))
myEll = ellipsoid(pos=vector(2,3,4),size=vector(1,2,3))
myExtrusion = extrusion(path=paths.circle(pos=vec(-6,2,0)), shape=shapes.rectangle(width=0.4, height=0.2),
                        up=vec(1,0,0), radius=2, color=color.cyan)
myHelix = helix(pos=vector(0,2,1), axis=vector(5,0,0), radius=0.5)
myPoints = points(pos=[vector(6,3,0), vector(2,1,0)], radius=5,color=color.red)

#triangle
a = vertex( pos=vec(3,-2,1) )
b = vertex( pos=vec(2,-1,1) )
c = vertex( pos=vec(1,0,2) )
myTriangle = triangle(v0=a, v1=b, v2=c)

#Lighting
myLamp = local_light(pos=vector(2,3,4),color=color.yellow)
myLight = distant_light(direction=vector(10,10,10), color=color.red)
myLabel = label(pos=myEll.pos, text='Lamp', xoffset=20, yoffset=50, space=30, height=16, border=4,font='sans')
myLabel = label(pos=mySphere.pos, text='Light', xoffset=20, yoffset=50, space=30, height=16, border=4,font='sans')
