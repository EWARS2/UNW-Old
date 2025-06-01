# Declarations
from contextlib import suppress
import viz

# Get path to load environment
load_msg  = "(Examples: piazza.osgb, dojo.osgb, ground.osgb)"
load_msg += "\nEnter path to environment file to load:"
env_path = input(load_msg)

# Create environment
env_obj = viz.addChild(env_path)
with suppress(ValueError): viz.MainWindow.fov(float(input("FOV:")))
with suppress(ValueError): viz.setMultiSample(int(input("FSAA Antialiasing Level:")))
viz.MainView.collision(bool(input("Collision? (Leave blank if false)")))
viz.go()  # Create window