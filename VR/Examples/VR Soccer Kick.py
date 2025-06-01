#declarations
import viz
import vizshape
import vizact

#actions
def fkick():
    typical_move = vizact.moveTo([4.5,0.2,1.5], time = 0.7)
    soccer.addAction(typical_move)

def mkick():
    typical_move = vizact.moveTo([4.5,0.2,8.5], time = 0.7)
    soccer.addAction(typical_move)

#environment
viz.go()
viz.MainWindow.fov(60)
ground = viz.addChild('ground.osgb')
vizshape.addAxes()

#ball
soccer = viz.addChild('soccerball.ogb')
soccer.setPosition([4.5, 0.2, 8.5])
soccer.setScale([1.5,1.5,1.5])

#avatars
male = viz.addAvatar('vcc_male.cfg')
male.setPosition([4.5,0,1])
male.setEuler([0,0,0])
male.state(6)
female = viaz.addAvatar('vcc_female.cfg')
female.setPosition([4.5,0,9])
female.setEuler([180,0,0])
female.state(6)

#interactions
vizact.onkeydown('f', fkick)
vizact.onkeydown('m',mkick)