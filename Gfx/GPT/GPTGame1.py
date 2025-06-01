from vpython import *

# Create a scene
scene = canvas(title="3D Game: Move the Ball",
               width=800, height=600,
               center=vector(0, 0, 0),
               background=color.cyan)

# Add ground
ground = box(pos=vector(0, -0.5, 0), size=vector(20, 1, 20), color=color.green)

# Add a ball (player object)
ball = sphere(pos=vector(0, 0, 0), radius=0.5, color=color.red)

# Add obstacles
obstacles = []
for i in range(5):
    obstacle = box(pos=vector((i + 1) * 3, 0, (i % 2) * 6 - 3),
                   size=vector(1, 1, 1), color=color.blue)
    obstacles.append(obstacle)

# Ball velocity and controls
ball_velocity = vector(0, 0, 0)
speed = 0.2


# Keyboard input handlers
def keydown(event):
    global ball_velocity
    if event.key == "up":
        ball_velocity = vector(0, 0, -speed)
    elif event.key == "down":
        ball_velocity = vector(0, 0, speed)
    if event.key == "left":
        ball_velocity = vector(-speed, 0, 0)
    elif event.key == "right":
        ball_velocity = vector(speed, 0, 0)


def keyup(event):
    global ball_velocity
    if event.key in ["up", "down", "left", "right"]:
        ball_velocity = vector(0, 0, 0)


# Attach handlers to the scene
scene.bind('keydown', keydown)
scene.bind('keyup', keyup)

# Game loop
while True:
    rate(60)  # Limit the game loop to 60 frames per second
    ball.pos += ball_velocity

    # Check for collisions with obstacles
    for obstacle in obstacles:
        if mag(ball.pos - obstacle.pos) < ball.radius + 0.5:  # Collision threshold
            ball.color = color.orange  # Change color on collision
