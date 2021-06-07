import math
import random
#Task 1a

def solveDerivative(x):
	result = 400 * math.pow(x, 3) + (2-400*(x+1)) * x-2 #Calculate Derivative f'(x)
	print('f\'(', x,') =', result) #print result
	return result

n = 20
learningRate = 0.000001 #needs to be surprisingly small for decent results. Larger leads to fast, unaccurate conclusions, smaller rarely comes to a conclusion within 10k iterations.
currentX = random.randint(1, n-1) #Randomly determine starting x
for unused in range(1, 10000): #10k iterations
	curResult = solveDerivative(currentX) #
	diff = -learningRate * curResult
	currentX += diff

print("final X is", currentX, "; with f\'(",currentX,")= ", solveDerivative(currentX) )

  # for count in range(1,20):
  #   print list[count]
  #   if count % 10 == 0:
  #      print 'did ten'