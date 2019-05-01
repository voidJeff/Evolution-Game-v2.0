import random
from Creature import *

def fitness(data):
	scoreList = []
	data.creatureList.sort(key = lambda creature : creature.foodEaten, reverse=True)
	data.creatureList1.sort(key = lambda creature : creature.foodEaten, reverse=True)
	for creature in data.creatureList:
		scoreList.append(creature.health)
	print(scoreList)

def reproduce(creature):
	dna = creature.getDNA()
	dna = mutate(dna)
	return Creature(creature.cx,creature.cy,2+dna[0]/4,dna[1]*20,dna[2]*150,creature.color,dna[3],dna[4])

def mutate(dna, mutationRate=50):
	#colorchange = r,g,b #implement later
	while random.uniform(0,100) < mutationRate:
		for i in range(random.randint(0,4)):
			i = random.randint(0,4)
			j = random.randint(0,4)
			if dna[i] > 1:
				mutation = random.uniform(0,1)
				dna[i] -= mutation
				dna[j] += mutation
	return dna

def selectBestCreatures(data):
	fitness(data)
	population = len(data.creatureList)
	halfPopulation = population // 2
	for i in range(population):
		if i <= halfPopulation and random.randint(0,100) < 90:
			creature = data.creatureList[i]
			if creature.health > 50: 
				data.reproducePool.append(creature)
		elif i > halfPopulation and random.randint(0,100) < 10:
			data.reproducePool.append(data.creatureList[i])

	population1 = len(data.creatureList1)
	halfPopulation1 = population1 // 2
	for i in range(population1):
		if i <= halfPopulation1 and random.randint(0,100) < 90:
			creature = data.creatureList1[i]
			if creature.health > 50:
				data.reproducePool1.append(creature)
		elif i > halfPopulation1 and random.randint(0,100) < 10:
			data.reproducePool1.append(data.creatureList1[i])

def nextGeneration(data):
	selectBestCreatures(data)

	for creature in data.reproducePool:
		for i in range(int(creature.children)):
			data.creatureList.append(reproduce(creature))
	data.reproducePool = []

	for creature in data.reproducePool1:
		for i in range(int(creature.children)):
			data.creatureList1.append(reproduce(creature))
	data.reproducePool1 = []



