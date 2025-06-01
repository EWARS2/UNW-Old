# Author: Ethan Reed
# Class: Programming I: Java
# Professor Jonathan Zderad

from vpython import *
from random import uniform

BOUNDARY = 10

scene = canvas(title="Program #2. Draw an interesting animated 3D image using vpython.")

label(pos=vector(0, -BOUNDARY, 0), text='Windows XP "Pipes" screensaver recreation')
my_sphere = sphere(make_trail=True, radius=0.2)
pos = [0,0,0]

while scene.visible:
    for i in range(len(pos)):
        rate(10)
        pos[i] = uniform(-BOUNDARY, BOUNDARY)
        my_sphere.pos = vector(pos[0], pos[1], pos[2])