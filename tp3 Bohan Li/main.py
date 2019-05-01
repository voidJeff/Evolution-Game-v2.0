from tkinter import *
'''
########### Model #############
def init(data):
	data.mode = "splashScreen"
	data.creatureList = []
	data.score = 0
	data.foodCount = 0
	# TODO: add code here
	data.shrinkFoodList = []
	data.explosiveFoodList = []
	data.foodList = []
	data.timerCount = 0
	data.rotateAngle = 15
	data.speed = 3
	data.health = 5
	data.sex = 3
	#data.agility = 1
	data.points = 20
	data.selection = 1
	data.firstTime = True
	data.tracking = {}
	data.showInfo = False
'''
###################################
###########Splash Screen###########
from SplashScreen import *

###################################
###########Game Screen#############
from GameScreen import *

###################################
############Setting Screen#########
from SettingScreen import *
###################################


#############################
# copied from course website "mode demo": https://www.cs.cmu.edu/~112/notes/notes-animations-part2.html
############################
def mousePressed(event, data):
	if (data.mode == "splashScreen"): splashScreenMousePressed(event, data)
	elif (data.mode == "playGame"):   playGameMousePressed(event, data)
	elif (data.mode == "setting"):       settingMousePressed(event, data)

def keyPressed(event, data):
	if (data.mode == "splashScreen"): splashScreenKeyPressed(event, data)
	elif (data.mode == "playGame"):   playGameKeyPressed(event, data)
	elif (data.mode == "setting"):       settingKeyPressed(event, data)

def timerFired(data):
	if (data.mode == "splashScreen"): splashScreenTimerFired(data)
	elif (data.mode == "playGame"):   playGameTimerFired(data)
	elif (data.mode == "setting"):       settingTimerFired(data)

def redrawAll(canvas, data):
	if (data.mode == "splashScreen"): splashScreenRedrawAll(canvas, data)
	elif (data.mode == "playGame"):   playGameRedrawAll(canvas, data)
	elif (data.mode == "setting"):       settingRedrawAll(canvas, data)


################################fov is the next step###########################
###############################################################################
###############################################################################




#################Run Function######
# run function copied fron HW8 starter file: https://www.cs.cmu.edu/~112/notes/hw8.html
def run(width=300, height=300):
	def redrawAllWrapper(canvas, data):
		canvas.delete(ALL)
		canvas.create_rectangle(0, 0, data.width, data.height,
								fill='black', width=0)
		redrawAll(canvas, data)
		canvas.update()

	def mousePressedWrapper(event, canvas, data):
		mousePressed(event, data)
		redrawAllWrapper(canvas, data)

	def keyPressedWrapper(event, canvas, data):
		keyPressed(event, data)
		redrawAllWrapper(canvas, data)

	def timerFiredWrapper(canvas, data):
		timerFired(data)
		redrawAllWrapper(canvas, data)
		# pause, then call timerFired again
		canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
	# Set up data and call init
	class Struct(object): pass
	data = Struct()
	data.width = width
	data.height = height
	data.timerDelay = 1 # milliseconds
	root = Tk()
	init(data)
	# create the root and the canvas
	canvas = Canvas(root, width=data.width, height=data.height)
	canvas.configure(bd=0, highlightthickness=0)
	canvas.pack()
	# set up events
	root.bind("<Button-1>", lambda event:
							mousePressedWrapper(event, canvas, data))
	root.bind("<Key>", lambda event:
							keyPressedWrapper(event, canvas, data))
	timerFiredWrapper(canvas, data)
	# and launch the app
	root.mainloop()  # blocks until window is closed
	print("bye!")

run(800, 800)