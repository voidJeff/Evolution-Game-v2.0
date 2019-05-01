
def splashScreenMousePressed(event, data):
	pass

def splashScreenKeyPressed(event, data):
	data.mode = "setting"

def splashScreenTimerFired(data):
	pass

def splashScreenRedrawAll(canvas, data):
	canvas.create_rectangle(0,0,data.width,data.height,fill='black')
	canvas.create_text(data.width/2, data.height/2-20,
					   text="Evolution Game", font="Arial 44 bold", fill = 'white')
	canvas.create_text(data.width/2, data.height/2+20,
					   text="Press any key to play", font="Arial 20", fill = 'white')