# Author: Ethan Reed
# Class: Programming I: Java
# Professor Jonathan Zderad

from vpython import *

scene = canvas(title="Program #1. Draw an interesting 3D image using vpython.")

def old_ea_logo():
    my_cube = box(pos=vector(-9, 0, 0), size=vector(10,10,10), opacity=0.5)
    my_sphere = sphere(pos=vector(0, 0, 0), size=vector(10,10,10), opacity=0.5)
    my_cone = cone(pos=vector(6, -5, 0), size=vector(10,10,10), opacity=0.5, up=vector(-1,0,0))
    label(pos=vector(0, -5, 0), text="The old\nElectronic Arts logo", xoffset=20, yoffset=50, height=20, color=color.white)
    return compound([my_cube, my_sphere, my_cone])

logo = old_ea_logo()

while scene.visible:
    rate(60)
    logo.rotate(0.01)