##########################################
# Original Code by Jack Bowman
# Final Code by Dr. Jonathan Zderad, 3/19/23
# This shows a bike moving up and backwards
##########################################

from vpython import *

class Bike:
    def __init__(self, pos=vector(0, 0, 0)):
        # frame
        self.frame1 = cylinder(pos=pos + vector(0, 0, -3), axis=vector(10, 0, 0), radius=1, length=10, color=color.blue)
        self.frame2 = cylinder(pos=pos + vector(0, 0, 3), axis=vector(10, 0, 0), radius=1, length=10, color=color.blue)
        self.frame3 = cylinder(pos=pos + vector(0, 0, -3.5), axis=vector(0, 0, 2), radius=1, length=7, color=color.blue)
        self.frame4 = cylinder(pos=pos + vector(0, 0, 0), axis=vector(0.5, 2, 0), radius=1, length=14, color=color.blue)
        self.frame5 = cylinder(pos=pos + vector(-15, 0, -3), axis=vector(0.75, 2, 0), radius=1, length=10,
                               color=color.blue)
        self.frame6 = cylinder(pos=pos + vector(-15, 0, 3), axis=vector(0.75, 2, 0), radius=1, length=10,
                               color=color.blue)
        self.frame7 = cylinder(pos=pos + vector(-11, 10, -3.5), axis=vector(0, 0, 2), radius=1, length=7,
                               color=color.blue)
        self.frame8 = cylinder(pos=pos + vector(-11, 10, 0), axis=vector(0.75, 2, 0), radius=1, length=14,
                               color=color.blue)
        self.frame9 = cylinder(pos=pos + vector(0, 0, 0), axis=vector(-2, 2, 0), radius=1, length=15, color=color.blue)
        self.handles = cylinder(pos=pos + vector(-5, 23, -7.5), axis=vector(0, 0, 2), radius=1, length=14,
                                color=color.black)
        # seat
        self.seat = box(pos=pos + vector(2, 14, 0), axis=vector(0, 0, 0), length=10, width=6, height=2,
                        color=color.black)
        # wheels/axles
        self.front_wheel = cylinder(pos=pos + vector(-15, 0, -1), axis=vector(0, 0, 2), radius=7, color=color.black)
        self.front_axle = cylinder(pos=pos + vector(-15, 0, -3.5), axis=vector(0, 0, 2), radius=1, length=7,
                                   color=color.white)
        self.back_wheel = cylinder(pos=pos + vector(10, 0, -1), axis=vector(0, 0, 2), radius=7, color=color.black)
        self.back_axle = cylinder(pos=pos + vector(10, 0, -3.5), axis=vector(0, 0, 2), radius=1, length=7,
                                  color=color.white)
    def move(self):
        v = vector(-1, 0, 0)
        w = vector(-0.001, 0, 0)
        global dt
        self.front_wheel.pos += w * dt
        self.back_wheel.pos += w * dt
        self.frame1.pos += v * dt
        self.frame2.pos += v * dt
        self.frame3.pos += v * dt
        self.frame4.pos += v * dt
        self.frame5.pos += v * dt
        self.frame6.pos += v * dt
        self.frame7.pos += v * dt
        self.frame8.pos += v * dt
        self.frame9.pos += v * dt
        self.handles.pos += v * dt
        self.seat.pos += v * dt
        self.front_wheel.pos += v * dt
        self.front_axle.pos += v * dt
        self.back_wheel.pos += v * dt
        self.back_axle.pos += v * dt

def positive(event):
    global dt
    dt += 1
def negative(event):
    global dt
    dt -= 1
def stop(event):
    global dt
    dt = 0

#Mainline
dt = 0
scene = canvas(background=color.gray(0.7))
bike = Bike(vector(200, 0, 0))
box(pos=vector(0, 0, 0), axis=vector(-250, 0, 0), width=100, length=10, height=100, color=color.green)
button(bind=negative, text = 'Negative')
button(bind=stop, text = 'Stop')
button(bind=positive, text = 'Positive')
while True:
    rate(10)
    bike.move()