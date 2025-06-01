#declarations
import random
import viz
import vizshape
import vizact
#actions
#create environment
viz.go()
viz.MainWindow.fov(60)
envir = viz.addChild('ground.osgb')
vizshape.addAxes()
#create plant
plant1 = viz.addChild('plant.osgb')
plant1.setPosition([4, 0, 6])
plant1.setScale([1.0,1.0,1.0])
#create soccerball
sball = viz.addChild('soccerball.osgb')
sball.setPosition([-2, 0.2, 3])
sball.setScale([2.0,2.0,2.0])

#create basketball
bball = viz.addChild('basketball.osgb')
bball.setPosition([-4, 0.2, 3])
bball.setScale([2.0,2.0,2.0])
#create volleyball
vball = viz.addChild('volleyball.osgb')
vball.setPosition([-1, 0.2, -3])
vball.setScale([2.0,2.0,2.0])
#create pigeon
pigeon = viz.addAvatar('pigeon.cfg')
pigeon.setPosition([3,0,2])
pigeon.setScale([3.0,3.0,3.0])
#create female
female = viz.addAvatar('vcc_female.cfg')
female.setPosition([4.5,0,9])
#create male
male = viz.addAvatar('vcc_male.cfg')
male.setPosition([4.5, 0, 7])