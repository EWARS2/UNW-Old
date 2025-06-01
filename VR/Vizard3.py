# Declarations
from contextlib import suppress
import viz
import vizact

def create_obj(filename, position=[0,0,0], scale=[1.0,1.0,1.0]):
	my_obj = viz.addChild(filename)
	my_obj.setPosition(position)
	my_obj.setScale(scale)
	return my_obj

# Create environment
env_obj = viz.addChild("ground.osgb")
viz.MainView.collision(True)
viz.go()  # Create window

# Create objects
thing1 = create_obj("vcc_male.cfg", [-1,0,10])
thing2 = create_obj("pigeon.cfg", [ 0,0,10])
thing3 = create_obj("vcc_female.cfg", [ 1,0,10])

# Attach button events
vizact.onkeydown('1', thing1.addAction, vizact.walkTo([20,0,20]))
vizact.onkeydown('2', thing2.addAction, vizact.sizeTo([10,10,10], speed=1))
vizact.onkeydown('3', thing3.state, 4)