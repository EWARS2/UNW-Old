#declarations
import viz
import vizshape
import vizact
fpos = 7.0
mpos = 3.0

#actions
def fmovefor():
    global fpos
    fpos -= 0.3
    typical_move = vizact.moveTo([4.5,0.2,fpos], time = 0.3)
    female.addAction(typical_move)
def mmovefor():
    global mpos
    mpos += 0.3
    typical_move = vizact.moveTo([4.5,0.2,mpos], time = 0.3)
    male.addAction(typical_move)

def fmoveback():
    global fpos
    fpos += 0.3
    typical_move = vizact.moveTo([4.5,0.2,fpos], time = 0.3)
    female.addAction(typical_move)

def mmoveback():
    global mpos
    mpos -= 0.3
    typical_move = vizact.moveTo([4.5,0.2,mpos], time = 0.3)
    male.addAction(typical_move)
    
def ffight():
    female.state(6)
    
def mfight():
    male.state(6)

def fjump():
    female.state(7)
    
def mjump():
    male.state(7)
    
def fdrop():
    female.state(8)
    
def mdrop():
    male.state(8)

#environment
viz.go()
viz.MainWindow.fov(60)
ground = viz.addChild('ground.osgb')
vizshape.addAxes()

#avatars
male = viz.addAvatar('vcc_male.cfg')
male.setPosition([4.5, 0, mpos])
male.setEuler([0,0,0])
male.state(1)
female = viz.addAvatar('vcc_female.cfg')
female.setPosition([4.5,0,fpos])
female.setEuler([180,0,0])
female.state(1)

#interactions
vizact.onkeydown('q',fmovefor)
vizact.onkeydown('w',fmoveback)
vizact.onkeydown('a',ffight)
vizact.onkeydown('s',fjump)
vizact.onkeydown('z',fdrop)

vizact.onkeydown('y',mmovefor)
vizact.onkeydown('u',mmoveback)
vizact.onkeydown('h',mfight)
vizact.onkeydown('j',mjump)
vizact.onkeydown('n',mdrop)
