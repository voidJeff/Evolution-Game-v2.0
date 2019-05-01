import random
class Food(object):
	# Model
	def __init__(self, cx, cy, r):
		self.cx = cx
		self.cy = cy
		self.r = r

	def __repr__(self):
		return 'food'

	# View
	def draw(self, canvas, color="green1"):
		canvas.create_oval(self.cx - self.r, self.cy - self.r,
						   self.cx + self.r, self.cy + self.r,
						   fill=color)

def createNewFoods(data):
	data.timerCount += 1
	if data.timerCount == 20:
		data.foodList.append(makeFood(data))
		data.foodCount += 1	
		data.timerCount = 0

def makeFood(data):
	# Generates a normal food heading in a random direction
	rLow, rHigh = 3, 4
	r = random.randint(rLow, rHigh)
	x = random.randint(r+1, data.width-r-1) 
	y = random.randint(r+1, data.height-r-1)
	return (Food(x, y, r))