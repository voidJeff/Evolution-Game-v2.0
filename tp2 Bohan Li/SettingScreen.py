def settingMousePressed(event, data):
	pass

def settingKeyPressed(event, data):
	if event.keysym == "Right":
		data.selection += 1

	elif event.keysym == "Left":
		data.selection -= 1

	if data.selection < 1: data.selection = 5
	elif data.selection > 5: data.selection = 1

	if event.keysym == "Up" and data.speed + data.health + data.sex + data.agility + data.vision < 20:
		if data.selection == 1: 
			data.speed += 1
			minusPoint(data)
		elif data.selection == 2: 
			data.health += 1
			minusPoint(data)
		elif data.selection == 3: 
			data.sex += 1
			minusPoint(data)
		elif data.selection == 4: 
			data.agility += 1
			minusPoint(data)
		elif data.selection == 5: 
			data.vision += 1
			minusPoint(data)
	elif event.keysym == "Down":
		if data.selection == 1 and data.speed > 1: 
			data.speed -= 1
			data.points += 1
		elif data.selection == 2 and data.health > 1: 
			data.health -= 1
			data.points += 1
		elif data.selection == 3 and data.sex > 1: 
			data.sex -= 1
			data.points += 1
		elif data.selection == 4 and data.agility > 1: 
			data.agility -= 1
			data.points += 1
		elif data.selection == 5 and data.vision > 1: 
			data.vision -= 1
			data.points += 1
	elif event.keysym == "space":
		data.mode = "playGame"
#############################################
	if event.keysym == "d":
		data.selection1 += 1
	elif event.keysym == "a":
		data.selection1 -= 1

	if data.selection1 < 1: data.selection1 = 5
	elif data.selection1 > 5: data.selection1 = 1

	if event.keysym == "w" and data.speed1 + data.health1 + data.sex1 + data.agility1 + data.vision1 < 20:
		if data.selection1 == 1: 
			data.speed1 += 1
			minusPoint1(data)
		elif data.selection1 == 2: 
			data.health1 += 1
			minusPoint1(data)
		elif data.selection1 == 3: 
			data.sex1 += 1
			minusPoint1(data)
		elif data.selection1 == 4: 
			data.agility1 += 1
			minusPoint1(data)
		elif data.selection1 == 5: 
			data.vision1 += 1
			minusPoint1(data)
	elif event.keysym == "s":
		if data.selection1 == 1 and data.speed1 > 1: 
			data.speed1 -= 1
			data.points1 += 1
		elif data.selection1 == 2 and data.health1 > 1: 
			data.health1 -= 1
			data.points1 += 1
		elif data.selection1 == 3 and data.sex1 > 1: 
			data.sex1 -= 1
			data.points1 += 1
		elif data.selection1 == 4 and data.agility1 > 1: 
			data.agility1 -= 1
			data.points1 += 1
		elif data.selection1 == 5 and data.vision1 > 1: 
			data.vision1 -= 1
			data.points1 += 1
##############################################
def settingTimerFired(data):
	pass

def settingRedrawAll(canvas, data):
	canvas.create_rectangle(0,0,data.width, data.height,fill='black')
	canvas.create_text(data.width/2, 40,
					   text="Settings", font="Courier 30 bold", fill='white')
	canvas.create_text(data.width/2, data.height-80,
					   text="To select: Player1: <-A D->  Player2: arrow keys", font="Courier 20",fill='white')
	canvas.create_text(data.width/2, data.height-55,
					   text="To alter: Player1: W S  Player2: arrow keys", font="Courier 20",fill='white')
	canvas.create_text(data.width/2, data.height-25,
					   text="Press SPACE to start simulation", font="Courier 20 bold",fill='white')
###################################################################################
	if data.color1 == (0,0,0): c1 = 'white'
	else: c1 = getColor(*data.color1)
	canvas.create_text(data.width/6, data.height/2 - 160,
					   text="Speed", font="Helvetica 30 bold",fill=c1)
	canvas.create_text(data.width/6, data.height/2 - 60,
					   text=str(round(data.speed,2)), font="Courier 40 bold",fill='white')

	canvas.create_text(data.width*2/6, data.height/2 - 160,
					   text="Health", font="Helvetica 30 bold",fill=c1)
	canvas.create_text(data.width*2/6, data.height/2 - 60,
					   text=str(round(data.health,2)), font="Courier 40 bold",fill='white')

	canvas.create_text(data.width*3/6, data.height/2 - 160,
					   text="Children", font="Helvetica 30 bold",fill=c1)
	canvas.create_text(data.width*3/6, data.height/2 - 60,
					   text=str(round(data.sex,2)), font="Courier 40 bold",fill='white')

	canvas.create_text(data.width*4/6, data.height/2 - 160,
					   text="Agility", font="Helvetica 30 bold",fill=c1)
	canvas.create_text(data.width*4/6, data.height/2 - 60,
					   text=str(round(data.agility,2)), font="Courier 40 bold",fill='white')

	canvas.create_text(data.width*5/6, data.height/2 - 160,
					   text="Vision", font="Helvetica 30 bold",fill=c1)
	canvas.create_text(data.width*5/6, data.height/2 - 60,
					   text=str(round(data.vision,2)), font="Courier 40 bold",fill='white')

	canvas.create_text(data.width/2, data.height/5 - 15,
					   text = str(data.points), font="Courier 40 bold",fill='white')
	canvas.create_text(data.width/2, data.height/8,
					   text = 'Player 1 Points Left', font="Courier 20 bold",fill='white')
#####################################################################################
	if data.color2 == (0,0,0): c2 = 'white'
	else: c2 = getColor(*data.color2)
	canvas.create_text(data.width/6, data.height/2 + 140,
					   text="Speed", font="Helvetica 30 bold",fill=c2)
	canvas.create_text(data.width/6, data.height/2 + 240,
					   text=str(round(data.speed1,2)), font="Courier 40 bold",fill='white')

	canvas.create_text(data.width*2/6, data.height/2 + 140,
					   text="Health", font="Helvetica 30 bold",fill=c2)
	canvas.create_text(data.width*2/6, data.height/2 + 240,
					   text=str(round(data.health1,2)), font="Courier 40 bold",fill='white')

	canvas.create_text(data.width*3/6, data.height/2 + 140,
					   text="Children", font="Helvetica 30 bold",fill=c2)
	canvas.create_text(data.width*3/6, data.height/2 + 240,
					   text=str(round(data.sex1,2)), font="Courier 40 bold",fill='white')

	canvas.create_text(data.width*4/6, data.height/2 + 140,
					   text="Agility", font="Helvetica 30 bold",fill=c2)
	canvas.create_text(data.width*4/6, data.height/2 + 240,
					   text=str(round(data.agility1,2)), font="Courier 40 bold",fill='white')

	canvas.create_text(data.width*5/6, data.height/2 + 140,
					   text="Vision", font="Helvetica 30 bold",fill=c2)
	canvas.create_text(data.width*5/6, data.height/2 + 240,
					   text=str(round(data.vision1,2)), font="Courier 40 bold",fill='white')

	canvas.create_text(data.width/2, data.height/5 - 15 + 300,
					   text = str(data.points1), font="Courier 40 bold",fill='white')
	canvas.create_text(data.width/2, data.height/8 + 300,
					   text = 'Player 2 Points Left', font="Courier 20 bold",fill='white')
#####################################################################################

	if data.selection == 1:
		x, y, r = data.width/6, data.height/2 - 160, 65
	elif data.selection == 2:
		x, y, r = data.width*2/6, data.height/2 - 160, 65
	elif data.selection == 3:
		x, y, r = data.width*3/6, data.height/2 - 160, 65
	elif data.selection == 4:
		x, y, r = data.width*4/6, data.height/2 - 160, 65
	elif data.selection == 5:
		x, y, r = data.width*5/6, data.height/2 - 160, 65

	canvas.create_rectangle(x-r,y-r,x+r,y+r, outline='white')

#####################################################################################

	if data.selection1 == 1:
		x, y, r = data.width/6, data.height/2 + 140, 65
	elif data.selection1 == 2:
		x, y, r = data.width*2/6, data.height/2 + 140, 65
	elif data.selection1 == 3:
		x, y, r = data.width*3/6, data.height/2 + 140, 65
	elif data.selection1 == 4:
		x, y, r = data.width*4/6, data.height/2 + 140, 65
	elif data.selection1 == 5:
		x, y, r = data.width*5/6, data.height/2 + 140, 65

	canvas.create_rectangle(x-r,y-r,x+r,y+r, outline='white')

def minusPoint(data):
	if data.points > 0:
		data.points -= 1

def minusPoint1(data):
	if data.points1 > 0:
		data.points1 -= 1

def getColor(r, g, b):
	return "#%02x%02x%02x" % (r, g, b)
