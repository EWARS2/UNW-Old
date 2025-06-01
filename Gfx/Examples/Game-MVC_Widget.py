#####################################################################################################
# Author: Jonathan Zderad
# Date: March 10, 2023
# This program models a primitive 3D snake game
# The user can move around a 3D grid with a trail
# Based upon "Python 3D Graphics Tutorial 21: Understanding and Using Widgets in Vpython"
#     by Paul McWhorter see (https://www.youtube.com/watch?v=PJKBrPkcoMo&t=2388s)
# This uses a Model/View/Controller Architecture
#####################################################################################################

from vpython import *
from time import sleep

# Model
def initializeModel():
    global pos, velocity
    pos = [0.5, 0.5, 0.5]
    velocity = [0.0, 0.0, 0.0]

def updatePosition():
    global pos, velocity
    if ((pos[0] + velocity[0])<= 10) and ((pos[0] + velocity[0])>= -10):
        pos[0] += velocity[0]
    if ((pos[1] + velocity[1])<= 10) and ((pos[1] + velocity[1])>= -10):
        pos[1] += velocity[1]
    if ((pos[2] + velocity[2])<= 10) and ((pos[2] + velocity[2])>= -10):
        pos[2] += velocity[2]

# View
def arrows():
    myArrow1 = arrow(pos=vector(0, 0, 0), axis=vector(1, 0, 0), color=color.red, length=10, shaftwidth=0.2)
    myArrow2 = arrow(pos=vector(0, 0, 0), axis=vector(0, 1, 0), color=color.red, length=10, shaftwidth=0.2)
    myArrow3 = arrow(pos=vector(0, 0, 0), axis=vector(0, 0, 1), color=color.red, length=10, shaftwidth=0.2)
    myArrow4 = arrow(pos=vector(0, 0, 0), axis=vector(-1, 0, 0), color=color.red, length=10, shaftwidth=0.2)
    myArrow5 = arrow(pos=vector(0, 0, 0), axis=vector(0, -1, 0), color=color.red, length=10, shaftwidth=0.2)
    myArrow6 = arrow(pos=vector(0, 0, 0), axis=vector(0, 0, -1), color=color.red, length=10, shaftwidth=0.2)

def buttons():
    button(bind=moveRight, text='right')
    button(bind=moveLeft, text='left')
    button(bind=moveUp, text='up')
    button(bind=moveDown, text='down')
    button(bind=moveForward, text='up')
    button(bind=moveBackward, text='down')
    button(bind=moveStop, text='stop')

def initializeObject():
    global pos
    global myPyramid1
    myPyramid1 = pyramid(make_trail=True, pos=vector(pos[0], pos[1], pos[2]), color=color.green, length=0.5, width=1.0,
                         height=1.0)

def moveObject():
    global myPyramid1
    global pos
    myPyramid1.pos = vector(pos[0],pos[1],pos[2])

#Control
def moveRight(event):
    global velocity
    velocity = [0.3, 0.0, 0.0]

def moveLeft(event):
    global velocity
    velocity = [-0.3, 0.0, 0.0]

def moveUp(event):
    global velocity
    velocity = [0.0, 0.3, 0.0]

def moveDown(event):
    global velocity
    velocity = [0.0, -0.3, 0.0]

def moveForward(event):
    global velocity
    velocity = [0.0, 0.0, 0.3]

def moveBackward(event):
    global velocity
    velocity = [0.0, 0.0, -0.3]

def moveStop(event):
    global velocity
    velocity = [0.0, 0.0, 0.0]

#Mainline
#Call Model Functions
initializeModel()

#Call View Functions
arrows()
buttons()
initializeObject()

#Animate
while True:
    updatePosition()  #Model Update
    moveObject()      #View Update
    sleep(0.05)