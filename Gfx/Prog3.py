# Author: Ethan Reed
# Class: Programming I: Java
# Professor Jonathan Zderad

from random import randint
from vpython import *

scene = canvas(title="Program #3.  Use a widget to create a simple 3D game using vpython."
                     "\nThe widget should allow the user to control one or more objects in the game.",
               background=color.cyan)

try:
    from convert_stl import stl_to_triangles
    filename = input(".STL file to use for map:")
    scale = float(input("Scale to use:"))
    world = stl_to_triangles(filename)
except ImportError:
    print("STL Importer could not be found, using sample map.")
    world = [
        triangle(v0=vertex(pos=vector(-100, -100, 0)),
                 v1=vertex(pos=vector(-100,  100, 0)),
                 v2=vertex(pos=vector( 100, -100, 0))),
        triangle(v0=vertex(pos=vector( 100, -100, 0)),
                 v1=vertex(pos=vector(-100,  100, 0)),
                 v2=vertex(pos=vector( 100,  100, 0)))
    ]
    scale = 10

print("WASD/Arrow keys to move, E/X to jump.")
print("No, vpython cannot read Space.")
print("My code tries to check for it anyways.")

def up():
    global press_up
    press_up = True

def down():
    global press_down
    press_down = True

def left():
    global press_left
    press_left = True

def right():
    global press_right
    press_right = True

def jump():
    global press_jump
    press_jump = True

def keydown(event):
    if event.key in ["up", "w"]:
        up()
    elif event.key in ["down", "s"]:
        down()
    if event.key in ["left", "a"]:
        left()
    elif event.key in ["right", "d"]:
        right()
    if event.key in ['space', 'e', 'x']:
        jump()

def keyup(event):
    global press_jump
    global press_up
    global press_down
    global press_left
    global press_right
    if event.key in ["space", "e", "x"]:
        press_jump = False
    if event.key in ["up", "w"]:
        press_up = False
    if event.key in ["down", "s"]:
        press_down = False
    if event.key in ["left", "a"]:
        press_left = False
    if event.key in ["right", "d"]:
        press_right = False

def is_point_in_dim(point, min_vec, max_vec, pad):
    x_within = min_vec.x - pad <= point.x <= max_vec.x
    y_within = min_vec.y - pad <= point.y <= max_vec.y
    z_within = min_vec.z - pad <= point.z <= max_vec.z
    return x_within and y_within and z_within

def triangle_dim(tri):
    nx = min(tri.v0.pos.x, tri.v1.pos.x, tri.v2.pos.x)
    ny = min(tri.v0.pos.y, tri.v1.pos.y, tri.v2.pos.y)
    nz = min(tri.v0.pos.z, tri.v1.pos.z, tri.v2.pos.z)
    xx = max(tri.v0.pos.x, tri.v1.pos.x, tri.v2.pos.x)
    xy = max(tri.v0.pos.y, tri.v1.pos.y, tri.v2.pos.y)
    xz = max(tri.v0.pos.z, tri.v1.pos.z, tri.v2.pos.z)
    return [vec(nx,ny,nz), vec(xx,xy,xz)]

# TODO: This probably could be a lot more optimized.
#  Why doesn't VPython have built-in collision detection????
#  This was such a pain to get working.
def collision(point, triangles):
    global padding
    for tri in triangles:
        dim_min, dim_max = triangle_dim(tri)
        if is_point_in_dim(point, dim_min, dim_max, padding):
            return True
    return False

# TODO: These values can be tuned to your liking.
speed = scale / 5
jump_height = scale / 2
gravity = scale / 40
gravity_cap = scale * 2
padding = gravity_cap

death_barrier_y = min(v.pos.y for tri in world for v in (tri.v0, tri.v1, tri.v2)) - padding
velocity = vec(0, 0, 0)
press_jump = False
press_left = False
press_right = False
press_up = False
press_down = False
scene.bind('keydown', keydown)
scene.bind('keyup', keyup)

# For some reason, some STLs are 90* sideways when imported.
# This code compounds the model, translates it,
# and then updates vertices for collision.
world_compound = compound(world)
world_compound.rotate(-pi/2)
for i in range(len(world)):
    world[i].v0.pos = world_compound.compound_to_world(world[i].v0.pos)
    world[i].v1.pos = world_compound.compound_to_world(world[i].v1.pos)
    world[i].v2.pos = world_compound.compound_to_world(world[i].v2.pos)

# Place objects at random triangle in world
player = box(pos=world[randint(0, len(world)-1)].v0.pos, size=vec(scale, scale, scale), color=color.red)
collectible = sphere(pos=world[randint(0, len(world)-1)].v0.pos, radius=scale, color=color.yellow)

while scene.visible:
    rate(30)
    player.pos += velocity

    # Movement
    # Yes, this code looks nutty.
    # Done this way to work with keydown/up events
    # and allow for diagonal movement
    velocity.x = velocity.z = 0
    if press_up:
        velocity.x += speed * scene.forward.x
        velocity.z += speed * scene.forward.z
    elif press_down:
        velocity.x += -speed * scene.forward.x
        velocity.z += -speed * scene.forward.z
    if press_left:
        velocity.x += speed * scene.forward.z
        velocity.z += -speed * scene.forward.x
    elif press_right:
        velocity.x += -speed * scene.forward.z
        velocity.z += speed * scene.forward.x

    # Collision
    # If touching ground
    if collision(player.pos, world):  # or player.pos.y <= 0:
        # Push player out of ground
        if velocity.y < 0:
            velocity.y = gravity

        # If jump button is pressed, jump.
        if press_jump:
            velocity.y = jump_height

    # If not touching ground
    else:
        # Gravity
        velocity.y -= gravity
        if velocity.y < -gravity_cap:
            velocity.y = -gravity_cap

    # Collectible collection code
    if mag(player.pos - collectible.pos) < collectible.radius + padding:
        collectible.pos = world[randint(0, len(world)-1)].v0.pos

    # Death barrier collision
    if player.pos.y < death_barrier_y:
        player.pos = world[randint(0, len(world) - 1)].v0.pos