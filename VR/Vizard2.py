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
thing1 = create_obj("pigeon.cfg", [-1,0,10])
thing2 = create_obj("pigeon.cfg", [ 0,0,10], [5,5,5])
thing3 = create_obj("pigeon.cfg", [ 1,0,10], [-5,2.5,-5])

# Attach timers
vizact.ontimer2(0.1, viz.PERPETUAL, thing1.addAction, vizact.moveTo([10,10,10], speed=0.1))
vizact.ontimer2(0.1, viz.PERPETUAL, thing2.addAction, vizact.sizeTo([100,100,100], speed=0.5))
vizact.ontimer2(0.1, viz.PERPETUAL, thing3.addAction, vizact.spin(1,1,1,30))