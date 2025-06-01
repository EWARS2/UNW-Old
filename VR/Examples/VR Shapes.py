#declarations
import random
import viz
import vizshape
import vizact

#create environment
viz.go()
viz.MainWindow.fov(60)
piazza = viz.addChild('ground.osgb')
vizshape.addAxes()

box = vizshape.addBox([1,1,1],splitFaces=False,pos=(0,0.5,0))
cylinder = vizshape.addCylinder(height=1.0,radius=0.5,topRadius=None,bottomRadius=None,
    axis=vizshape.AXIS_Y,slices=20,bottom=True,top=True, pos=(0,0.5,2.5))
torus = vizshape.addTorus(radius=0.5,tubeRadius=0.2, sides=40, slices=40, axis=vizshape.AXIS_Y, pos = (0,0.1,5))
pyramid = vizshape.addPyramid(base=(1.0,1.0),height=1.0,axis=vizshape.AXIS_Y,splitFaces=False, pos = (0,0,-2.5))
sphere = vizshape.addSphere(radius=0.5,slices=20,stacks=20,axis=vizshape.AXIS_Y, pos = (0,0.5,-5.0)) 