import vpython as vp

scene = vp.canvas()

# Create some objects in your scene
box = vp.box()

while scene.visible:
    vp.rate(30)  # Limit frame rate
    # Do something with your objects
    box.rotate(angle=0.01, axis=vp.vector(0, 1, 0))

print("Window closed")