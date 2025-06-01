#declarations
import viz
import vizshape

#actions
#create environment
str = "1 = Dojo\n" +  "2 = Gallery\n" + "3 = Ground\n" + "4 = Interior\n" + "5 = Piazza\n"
str = str + "6 = Day Sky\n" + "7 = Night Sky\n" + "What environment?"

choice = int(input(str))

viz.go()
viz.MainWindow.fov(60)
if choice == 1:
    envir = viz.addChild('dojo.osgb')
if choice == 2:
    envir = viz.addChild('gallery.osgb')
if choice == 3:
    envir = viz.addChild('ground.osgb')
if choice == 4:
    envir = viz.addChild('interior_design.osgb')
if choice == 5:
    envir = viz.addChild('piazza.osgb')
if choice == 6:
    envir = viz.addChild('sky_day.osgb')
if choice == 7:
    envir = viz.addChild('sky_night.osgb')

vizshape.addAxes()