from Track import *
from Car import *
from CarAI import *
from Monaco import setupMonaco
from Traces import clearTraces, saveTraces


lastperformance = 0
caramount = 20
# Race between two random cars
# Replace dummy network with your network later

track = setupMonaco()

cars = []
for i in range(caramount):
	cars.append(CarAI(track))

def step(car):
	if car.gameOver:
		pass
	else:
		car.control()
		car.move()
		car.updateScore()
		if car.checkCollision() or car.score > 2000 or (car.score+5)/car.age <(lastperformance * 0.4) or (car.score+5)/car.age <0.01:  #letztes or mit (car.score+5)/car.age < timescoreschnellstesautoletztegeneration/scorelimit *0.8 
			car.gameOver = True

clearTraces()

for generation in range(50):
	livingCars = len(cars)
	while livingCars > 0:
		livingCars = 0
		for car in cars:
			step(car)
			if not car.gameOver:
				if livingCars == 0:
					#print(car.score, car.gameOver, car.x, car.y)
					livingCars += 1
		# print(livingCars)
	cars.sort(key=lambda car: car.score, reverse = True)
	best = cars[0]
	best.nn.savenn()
	lastperformance = (best.score+5)/car.age 
	saveTraces(cars, generation)

	cars = []
	cars.append(CarAI(track))
	cars[0].nn = best.nn.clone()
	for i in range(1,caramount):
		cars.append(CarAI(track))
		cars[i].nn = best.nn.clone()
		cars[i].nn.randomAdjust(3*((i*i)/(caramount*caramount)))
	print("generation", generation + 1)
	print(best.score, best.age)


