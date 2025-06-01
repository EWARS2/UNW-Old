#declarations
import random
import viz
import vizshape
import vizact

#actions
def spinPlant(plant):
	typical_spin = vizact.spin(0,1,0,15)
	plant.addAction(typical_spin)

def walkFemale():
    walk1 = vizact.walkTo([4.5, 0,-40])
    vizact.ontimer2(0.5,0,female.addAction,walk1)

def walkMale():
    walk2 = vizact.walkTo([3.5,0,-40])
    male.addAction(walk2)

def pigeonsFeed():
    random_speed = vizact.method.setAnimationSpeed(0,vizact.randfloat(0.7,1.5))
    random_walk = vizact.walkTo(pos=[vizact.randfloat(-4,4),0,vizact.randfloat(3,7)])
    random_animation = vizact.method.state(vizact.choice([1,3],vizact.RANDOM))
    random_wait = vizact.waittime(vizact.randfloat(5.0,10.0))
    pigeon_idle = vizact.sequence( random_speed, random_walk, random_animation, random_wait, viz.FOREVER)
    for pigeon in pigeons:
        pigeon.addAction(pigeon_idle)

#create environment
viz.go()
viz.MainWindow.fov(60)
piazza = viz.addChild('piazza.osgb')
vizshape.addAxes()

#create plants
plant1 = viz.addChild('plant.osgb')
plant1.setPosition([4, 0, 6])
plant1.setScale([3.0,3.0,3.0])
plant2 = viz.addChild('plant.osgb')
plant2.setPosition([8, 0, 6])
plant2.setScale([2.0,2.0,2.0])
vizact.ontimer(2,spinPlant,plant1)
vizact.ontimer(5,spinPlant,plant2)

#create pigeons
pigeons = []
for i in range(10):
    #Generate random values for position and orientation
    x = random.randint(-4,3)
    z = random.randint(4,8)
    yaw = random.randint(0,360)

    #Load a pigeon
    pigeon = viz.addAvatar('pigeon.cfg')

    #Set position, orientation, and state
    pigeon.setPosition([x,0,z])
    pigeon.setEuler([yaw,0,0])
    s = random.randint(0,10)
    pigeon.state(s)

    #Append the pigeon to a list of pigeons
    pigeons.append(pigeon)
    
#create avatars
male = viz.addAvatar('vcc_male.cfg')
male.setPosition([4.5, 0, 7])
male.setEuler([0,0,0])
male.state(14)
female = viz.addAvatar('vcc_female.cfg')
female.setPosition([4.5,0,9])
female.setEuler([180,0,0])
female.state(4)

#interactions - Binds actions to events
vizact.onkeydown('w',walkFemale)
vizact.onkeydown('m',walkMale)
vizact.onkeydown('p',pigeonsFeed)