from vpython import *

# Create the 3D scene
scene = canvas(title="3D Scene with VPython", width=800, height=600, center=vector(0, 1, 0))

# Add objects to the scene
floor = box(pos=vector(0, -0.5, 0), size=vector(10, 0.1, 10), color=color.green)
sphere_obj = sphere(pos=vector(-2, 1, 0), radius=1, color=color.blue)
rotating_cube = box(pos=vector(2, 1, 0), size=vector(1, 1, 1), color=color.red)

# Light source
distant_light(direction=vector(0, -1, -1), color=color.white)

# Add a label
label(pos=vector(0, 2, 0), text="VPython 3D Scene", xoffset=20, yoffset=50, height=20, color=color.white)

# Animation loop
angle = 0
while True:
    rate(60)  # Limit the loop to 60 frames per second
    angle += 0.03
    rotating_cube.rotate(angle=angle, axis=vector(0, 1, 0), origin=rotating_cube.pos)
