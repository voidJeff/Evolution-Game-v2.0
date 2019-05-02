from Creature import *
#from Food import *


def splashScreenMousePressed(event, data):
	pass

def splashScreenKeyPressed(event, data):
	data.mode = "setting"

	data.timerCount = 0
	data.foodList = []
	data.foodCount = 0


def splashScreenTimerFired(data):
	if data.splashBegin == True:
		data.splashBegin = False
		(r,g,b) = getRandomColor()
		while abs(r-g)+abs(g-b)+abs(b-r) < 250:
			(r,g,b) = getRandomColor()
		cColor = (r,g,b)
		tColor = (255-r, 255-g, 255-b)
		data.splashCreatureList.append(Predator(0, 0, 3, 150, 600, cColor, 3, 4))
		
		data.foodList.append(Food(data.width/2 - 225, data.height/2 - 46, 4))
		data.foodList.append(Food(data.width/2 + 118, data.height/2 - 46, 4))
		data.foodCount += 2

	if data.foodCount < 1:
		data.splashStartFood = True
	if data.splashStartFood:
		while data.foodCount < 5:
			createNewFoods(data)
	data.splashCreatureList[0].wrapAround(data.width, data.height)
	data.splashCreatureList[0].detectFood(data.foodList)
	data.splashCreatureList[0].move()
##################################################################
	index = 0
	while index < len(data.foodList):
		hit = False
		food = data.foodList[index]
		for creature in data.splashCreatureList:
			if creature.collidesWithFood(food):
				hit = True
				creature.foodEaten += 1
				data.foodCount -= 1
		if hit: data.foodList.remove(food)
		else: index += 1
##############################################################

	if data.splashScreenBlink == 80 or data.splashScreenBlink == 0:
		data.increment *= -1

	data.splashScreenBlink += data.increment
	

def splashScreenRedrawAll(canvas, data):
	
	
	canvas.create_text(data.width/2, data.height/2-30,
					   text="Survival of the Fit Enough", font="Courier 44", fill = 'white')
	
	a = int((data.splashScreenBlink / 80 + 0.4) * 255 / 1.4)
	canvas.create_text(data.width/2, data.height/2+30,
					   text="Press any key to begin", font="Courier 20", fill = getColor(a,a,a))
	cx = data.width/2 - 225
	cy = data.height/2 - 46
	r = 4
	canvas.create_oval(cx-r,cy-r,cx+r,cy+r, fill='black')


	cx1 = data.width/2 + 118
	cy1 = data.height/2 - 46

	canvas.create_oval(cx1-r,cy1-r,cx1+r,cy1+r, fill='black')
	

	for food in data.foodList:
		food.draw(canvas)
	for creature in data.splashCreatureList:
		creature.draw(canvas)
