## Creature class ##
import math, random
from Food import *
class Creature(object):
	# Model
	def __init__(self, cx, cy, speed, health, fov, color, agility, children):
		# A creature has a position and a current direction it faces
		self.cx = cx
		self.cy = cy
		self.speed = speed
		self.health = health
		self.maxHealth = health
		self.r = health
		self.fov = fov
		self.direction = random.randint(0,359)
		self.color = color
		self.agility = agility
		self.foodEaten = 0
		self.children = children
		self.isLastGen = False

	# View
	def draw(self, canvas):
		# Draws a cool-looking triangle-ish shape
		if self.health > 100: health = 100
		else: health = self.health
		color = getCreatureColor(health, self.color)
		ratio = (self.health - 100) / 100
		size = 6 * 2**(ratio)
		direction = math.radians(self.direction)
		angleChange = 2*math.pi/3
		numPoints = 3
		points = []
		for point in range(numPoints):
			points.append((self.cx + size*math.cos(direction + point*angleChange),
						   self.cy - size*math.sin(direction + point*angleChange)))
		points.insert(numPoints-1, (self.cx, self.cy))
		
		canvas.create_polygon(points, fill=color)

	def getDNA(self):
		return [(self.speed-2)*4, self.maxHealth/20, self.fov/150, self.agility, self.children]


	def showFOV(self, canvas):
		pass
		#canvas.create_oval(self.cx-self.fov, self.cy-self.fov, self.cx+self.fov,self.cy+self.fov, fill=None,outline='white')

	# Controller
	def rotate(self, numDegrees):
		self.direction = (self.direction + numDegrees) % 360

	def detectFood(self, foodList):
		foodInSight = []
		for food in foodList:
			#food = foodList[foodI]
			if distance(self.cx, self.cy, food.cx, food.cy) < self.fov + food.r:
				foodInSight.append(food)
			else:
				try: foodInSight.remove(food)
				except: pass
		try:
			foodInSight.sort(key = lambda food: distance(self.cx, self.cy, food.cx, food.cy))		
			food = foodInSight[0]
		except: return []
		foodAngle = math.atan2(self.cy-food.cy, food.cx-self.cx)
		foodAngle = math.degrees(foodAngle)%360
		deltaAngle = foodAngle - self.direction

		#self.direction = foodAngle
		#print(deltaAngle)
		#print(self.direction,foodAngle)
		delt = 1 + self.agility/3
		if foodAngle > self.direction:
			if foodAngle - self.direction > 180:
				self.rotate(-delt)
			elif foodAngle - self.direction < 180:
				self.rotate(delt)
			return foodInSight
		elif foodAngle < self.direction:
			if self.direction - foodAngle > 180:
				self.rotate(delt)
			elif self.direction - foodAngle < 180:
				self.rotate(-delt)
			return foodInSight
		return []

	def move(self):
		self.rotate(random.uniform(-1,1))
		self.cx += math.cos(math.radians(self.direction))*self.speed
		self.cy -= math.sin(math.radians(self.direction))*self.speed

	def collidesWithFood(self, other):
		# Check if the creature and food overlap at all
		if(not isinstance(other, Food)): # Other must be an Food
			return False
		else:
			dist = ((other.cx - self.cx)**2 + (other.cy - self.cy)**2)**0.5
			return dist < other.r

	def collidesWithWallY(self, width, height):
		# Check if the food hits the wall or overlaps it at all
		return self.cy <= 0 or self.cy >= height

	def collidesWithWallX(self, width, height):
		# Check if the food hits the wall or overlaps it at all
		return self.cx <= 0 or self.cx >= width 

	# TODO: add code here
	def reactToWallHit(self, screenWidth, screenHeight):
		if self.collidesWithWallY(screenWidth, screenHeight):
			self.cx -= math.cos(math.radians(self.direction))*self.speed
			self.cy += math.sin(math.radians(self.direction))*self.speed
			self.direction = (360 - self.direction)%360
		elif self.collidesWithWallX(screenWidth, screenHeight):
			self.cx -= math.cos(math.radians(self.direction))*self.speed
			self.cy += math.sin(math.radians(self.direction))*self.speed
			self.direction = (180 - self.direction)%360

	def isOffscreen(self, width, height):
		# Check if the creature has moved fully offscreen
		return (self.cx <= 0 or self.cx >= width) or \
			   (self.cy <= 0 or self.cy >= height)

	def wrapAround(self, width, height):
		if self.isOffscreen(width, height):
			self.cx %= width
			self.cy %= height


def spawnNewCreatures(data, cx, cy, color, playerNum):
	if playerNum == 1:
		data.creatureList.append(Creature(cx, cy, 2+data.speed/4, data.health*20, 150*data.vision, color, data.agility, data.sex))
	elif playerNum == 2:
		data.creatureList1.append(Creature(cx, cy, 2+data.speed1/4, data.health1*20, 150*data.vision1, color, data.agility1, data.sex1))


def distance(a, b, c, d):
	return math.sqrt((a-c)**2 + (b-d)**2)

# repurposed from an earlier homework
def getColor(r, g, b):
	return "#%02x%02x%02x" % (r, g, b)

def getCreatureColor(health, color):
	r, g, b = color 
	r, g, b = int(r * health / 100), int(g * health / 100), int(b * health / 100)
	return getColor(r, g, b)

def getRandomColor():
	r = random.randint(20,255)
	g = random.randint(20,255)
	b = random.randint(20,255)
	return (r, g, b)