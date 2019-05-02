from Food import *
from Creature import *
from GeneticAlgorithm import *
import random

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
	data.speed = 4
	data.health = 4
	data.sex = 4
	data.agility = 4
	data.vision = 4
	data.points = 0
	data.selection = 1
	data.firstTime = True
	data.tracking = {}
	data.showInfo = False
	data.color1 = (0, 0, 0)
	data.reproducePool = []
#################################
	data.creatureList1 = []
	data.score1 = 0
	data.foodCount1 = 0
	# TODO: add code here
	data.shrinkFoodList1 = []
	data.explosiveFoodList1 = []
	data.foodList1 = []
	data.timerCount1 = 0
	data.rotateAngle1 = 15
	data.speed1 = 4
	data.health1 = 4
	data.sex1 = 4
	data.agility1 = 4
	data.vision1 = 4
	data.points1 = 0
	data.selection1 = 1
	data.firstTime1 = True
	data.tracking1 = {}
	data.color2 = (0,0,0)
	data.reproducePool1 = []
	data.generationCounter = 0
	data.generation = 0
	data.winner = 0
	data.foodFreq = 20
	data.splashScreenBlink = 1
	data.increment = 1
	data.splashBegin = True
	data.splashCreatureList = []
	data.splashStartFood = False
	data.ratio = 0
	data.showChart = False
#################################

def playGameKeyPressed(event, data):
	if event.keysym == "Right":
		for creature in data.creatureList:
			creature.rotate(-4*data.rotateAngle)
	elif event.keysym == "Left":
		for creature in data.creatureList:
			creature.rotate(4*data.rotateAngle)
	elif event.keysym == "q":
		init(data)
	elif event.keysym == "Up":
		if data.foodFreq >= 4:
			data.foodFreq //= 2
	elif event.keysym == "Down":
		if data.foodFreq <= 128:
			data.foodFreq *= 2
	elif (event.keysym == 'e'):
		data.mode = "setting"
	elif (event.keysym == 'h'):
		data.showInfo = not data.showInfo
	elif (event.keysym == 'j'):
		data.showChart = not data.showChart
	# TODO: add code here

def playGameTimerFired(data):
	if data.firstTime:
		(r,g,b) = getRandomColor()
		while abs(r-g)+abs(g-b)+abs(b-r) < 250:
			(r,g,b) = getRandomColor()
		data.color1 = (r,g,b)
		data.color2 = (255-r, 255-g, 255-b)

		for i in range(2*data.sex):
			spawnNewCreatures(data, data.width/4, data.height/2, data.color1, 1)
		for i in range(2*data.sex1):
			spawnNewCreatures(data, data.width*3/4, data.height/2, data.color2, 2)
		for i in range(6):
			createNewFoods(data)
		data.firstTime = False
	# TODO: add code here
	if data.foodCount < 6: 
		createNewFoods(data)

	if data.creatureList != []:
		data.speed = data.creatureList[0].getDNA()[0]
		data.health = data.creatureList[0].getDNA()[1] 
		data.sex = data.creatureList[0].getDNA()[2]
		data.agility = data.creatureList[0].getDNA()[3]
		data.vision = data.creatureList[0].getDNA()[4]
	if data.creatureList1 != []:
		data.speed1 = data.creatureList1[0].getDNA()[0]
		data.health1 = data.creatureList1[0].getDNA()[1] 
		data.sex1 = data.creatureList1[0].getDNA()[2]
		data.agility1 = data.creatureList1[0].getDNA()[3]
		data.vision1 = data.creatureList1[0].getDNA()[4]

	data.generationCounter += 1
	if data.generationCounter == 600:
		data.generation += 1
		data.generationCounter = 0

		if len(data.creatureList) + len(data.creatureList1) < 100:
			for creature in data.creatureList:
				creature.isLastGen = True
			for creature in data.creatureList1:
				creature.isLastGen = True
			nextGeneration(data)




	for creature in data.creatureList:
		if creature.isLastGen: creature.health = 0
		if creature.health > 0: creature.health -= 0.95 ** (data.health) * 0.2
		#if creature.health > 300:
			#creature.health -= 225
			#for i in range(int(data.sex)):
				#pass
				#spawnNewCreatures(data, creature.cx, creature.cy, creature.color, 1)
		creatureI = data.creatureList.index(creature)
		creature.wrapAround(data.width, data.height)
		#creature.reactToWallHit(data.width, data.height)
		data.tracking[creature] = creature.detectFood(data.foodList)
		creature.move() # updates each creature's location

	for creature in data.creatureList1:
		if creature.isLastGen: creature.health = 0
		if creature.health > 0: creature.health -= 0.95 ** (data.health) * 0.2
		#if creature.health > 300:
			#creature.health -= 225
			#for i in range(int(data.sex1)):
				#pass
				#spawnNewCreatures(data, creature.cx, creature.cy, creature.color, 2)
		creatureI = data.creatureList1.index(creature)
		creature.wrapAround(data.width, data.height)
		#creature.reactToWallHit(data.width, data.height)
		data.tracking1[creature] = creature.detectFood(data.foodList)
		creature.move() # updates each creature's location

	
	hitDetection(data)

	i = 0
	while i < len(data.creatureList):
		creature = data.creatureList[i]
		if creature.health <= 0:
			data.creatureList.remove(creature)
			data.tracking.pop(creature)
		else:
			i += 1
	i = 0
	while i < len(data.creatureList1):
		creature = data.creatureList1[i]
		if creature.health <= 0:
			data.creatureList1.remove(creature)
			data.tracking1.pop(creature)
		else:
			i += 1
	##############################
	population1 = len(data.creatureList)
	population2 = len(data.creatureList1)
	if population1+population2 == 0:
		data.ratio = -1
	else:
		data.ratio = population1/(population1+population2)



	##############################

	if data.creatureList == [] and data.creatureList1 == []:
		data.winner = random.choice([1,2])
	if data.creatureList == []:
		data.winner = 2
	elif data.creatureList1 == []:
	 	data.winner = 1


def playGameMousePressed(event, data):
	rLow, rHigh = 10, 40
	r = random.randint(rLow, rHigh)
	data.foodList.append(Food(event.x, event.y, r))
	data.foodCount += 1

def playGameRedrawAll(canvas, data):
	#canvas.create_rectangle(0, 0, data.width, data.height, fill="black")


	for creature in data.creatureList:	
		creature.draw(canvas)
	
	for creature in data.creatureList1:	
		creature.draw(canvas)
	# TODO: add code here
	canvas.create_text(20, data.height, anchor="sw",
					   font="Courier 20", text="Player1 Score: " + str(data.score),fill=getColor(*data.color1))
	canvas.create_text(data.height, data.height, anchor="se",
					   font="Courier 20", text="Player2 Score: "+ str(data.score1),fill=getColor(*data.color2))
	

	for food in data.foodList:
		food.draw(canvas)

	canvas.create_text(data.width/2, 5, anchor='n', fill='white', text='generation '+str(data.generation),font="Courier 20")

	#r = 5
	#cx1 = data.width/4 + 2*r
	#cx2 = data.width/2
	#canvas.create_oval(cx1-r, data.height-3*r, cx1+r, data.height-1*r, fill=getColor(*data.color1))
	#canvas.create_oval(cx2-r, data.height-3*r, cx2+r, data.height-1*r, fill=getColor(*data.color2))

	################winner screen#########################################
	if data.winner == 1:
		canvas.create_text(data.width/2, data.height/2,font="Courier 30", text='Player '+str(data.winner)+' wins!!', fill=getColor(*data.color1))
		
	if data.winner == 2:
		canvas.create_text(data.width/2, data.height/2,font="Courier 30", text='Player '+str(data.winner)+' wins!!', fill=getColor(*data.color2))
	if data.winner != 0:
		canvas.create_text(data.width/2, data.height/2+40,font="Courier 20", text='Press Q to play again', fill='white')



	if data.showInfo:
		for creature in data.creatureList:
			foodInSight = data.tracking.get(creature, None)
			if foodInSight != None and foodInSight != []: 
				food = foodInSight[0]
				cx, cy = creature.cx, creature.cy
				fx, fy = food.cx, food.cy
				r = 150 + creature.foodEaten * 10
				if r > 255: r = 255
				canvas.create_line(cx, cy, fx, fy, fill=getColor(r,0,0))

		for creature in data.creatureList1:
			foodInSight = data.tracking1.get(creature, None)
			if foodInSight != None and foodInSight != []: 
				food = foodInSight[0]
				cx, cy = creature.cx, creature.cy
				fx, fy = food.cx, food.cy
				b = 150 + creature.foodEaten * 10
				if b > 255: b = 255
				canvas.create_line(cx, cy, fx, fy, fill=getColor(0,0,b))

	if data.showChart:
		m = 50
		rWidth = 60
		rHeight = 180
		if data.ratio == -1:
			canvas.create_rectangle(m,m,m+rWidth,m+rHeight,fill='grey',width=0)
		else:
			canvas.create_rectangle(m,m,m+rWidth,m+rHeight*data.ratio,fill=getColor(*data.color1),width=0)
			canvas.create_rectangle(m,m+rHeight*data.ratio,m+rWidth,m+rHeight,fill=getColor(*data.color2),width=0)
			if round(data.ratio*100,1) != 0.0:
				canvas.create_text(m+rWidth/2, m+rHeight*data.ratio/2, text=str(round(data.ratio*100,1))+"%",fill=getColor(*data.color2),font='Courier')
			if round((1-data.ratio)*100,1) != 0.0:
				canvas.create_text(m+rWidth/2, m+(rHeight*data.ratio+rHeight)/2, text=str(round((1-data.ratio)*100,1))+"%",fill=getColor(*data.color1),font='Courier')




def hitDetection(data):
	index = 0
	while index < len(data.foodList):
		hit = False
		food = data.foodList[index]
		for creature in data.creatureList:
			if creature.collidesWithFood(food):
				hit = True
				creature.foodEaten += 1
				creature.health += 50
				data.foodCount -= 1
				data.score += 1
				creatureI = data.creatureList.index(creature) 
		if hit: data.foodList.remove(food)
		else: index += 1

	index = 0
	while index < len(data.foodList):
		hit = False
		food = data.foodList[index]
		for creature in data.creatureList1:
			if creature.collidesWithFood(food):
				hit = True
				creature.foodEaten += 1
				creature.health += 50
				data.foodCount -= 1
				data.score1 += 1
				creatureI = data.creatureList1.index(creature) 
		if hit: data.foodList.remove(food)
		else: index += 1

def getColor(r, g, b):
	return "#%02x%02x%02x" % (r, g, b)