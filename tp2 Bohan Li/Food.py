import random
class Food(object):
	# Model
	def __init__(self, cx, cy, r):
		self.cx = cx
		self.cy = cy
		self.r = r
		self.color = (255,255,255) 

	def __repr__(self):
		return 'food'

	# View
	def draw(self, canvas):
		
		canvas.create_oval(self.cx - self.r, self.cy - self.r,
						   self.cx + self.r, self.cy + self.r,
						   fill=getColor(*self.color))

def createNewFoods(data):
	data.timerCount += 1
	if data.timerCount >= data.foodFreq:
		data.foodList.append(makeFood(data))
		data.foodCount += 1	
		data.timerCount = 0

def makeFood(data):
	# Generates a normal food heading in a random direction
	rLow, rHigh = 3,5
	r = random.uniform(rLow, rHigh)
	x = random.uniform(r+1, data.width-r-1) 
	y = random.uniform(r+1, data.height-r-1)
	return (Food(x, y, r))

def getRandomColor():
	r = random.randint(0,255)
	g = random.randint(0,255)
	b = random.randint(0,255)
	return (r, g, b)

def getColor(r, g, b):
	return "#%02x%02x%02x" % (r, g, b)