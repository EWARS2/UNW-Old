################################################
#  This is based upon a Jack Bowman Program
#  Addto to by Dr. Jonathan Zderad, 3/18/23
#  This allows the user to add random trees to make a forest
################################################

from vpython import *
import random

class Tree:
    def __init__(self, my_position=vector(0, -7, 0), my_scale = 12):
        self.position = my_position
        self.scale = my_scale

    def plot(self):
        #trunk
        self.trunk = cylinder(pos=vector(self.position.x, self.position.y, self.position.z),
                              axis=vector(0, 8 * self.scale, 0), radius=1.5 * self.scale, color=color.orange)
        #branches
        self.branch1 = cylinder(pos = vector(self.position.x,8*self.scale, self.position.z),
                                axis = vector(-4*self.scale,4*self.scale,0), radius = self.scale,
                                color=color.orange)
        self.branch2 = cylinder(pos=vector(self.position.x, 8 * self.scale, self.position.z),
                                axis=vector(4 * self.scale, 4 * self.scale, 0),
                                radius=self.scale, color=color.orange)
        self.branch3 = cylinder(pos=vector(self.position.x, 8 * self.scale, self.position.z),
                                axis=vector(0,4 * self.scale, 4 * self.scale),
                                radius=self.scale, color=color.orange)
        self.branch4 = cylinder(pos=vector(self.position.x, 8 * self.scale, self.position.z),
                                axis=vector(0, 4 * self.scale, -4 * self.scale),
                                radius=self.scale, color=color.orange)
        self.branch5= cylinder(pos=vector(self.position.x, 8 * self.scale, self.position.z),
                                axis=vector(0, 8 * self.scale,0),
                                radius=self.scale, color=color.orange)
        #leaves
        self.leaves1 = sphere(pos=vector(self.position.x - 4*self.scale, 12*self.scale,self.position.z),
                              radius = 4*self.scale, color=color.green)
        self.leaves2 = sphere(pos=vector(self.position.x + 4 * self.scale, 12 * self.scale, self.position.z),
                              radius=4 * self.scale, color=color.green)
        self.leaves3 = sphere(pos=vector(self.position.x, 12 * self.scale, self.position.z+ 4*self.scale),
                              radius=4 * self.scale, color=color.green)
        self.leaves4 = sphere(pos=vector(self.position.x, 12 * self.scale, self.position.z - 4*self.scale),
                              radius=4 * self.scale, color=color.green)
        self.leaves5 = sphere(pos=vector(self.position.x, 16 * self.scale, self.position.z),
                              radius=4 * self.scale, color=color.green)

def create_tree(event):
    global Tree1
    xpos = random.randrange(-100,100)
    ypos = 0
    zpos = random.randrange(-100,100)
    myscale = random.randrange(1,5)
    Tree1 = Tree (my_position= vector(xpos, ypos, zpos), my_scale= myscale)
    Tree1.plot()

#Mainline
button(bind=create_tree, text ='More')

#while True:
#    pass
#end Mainline