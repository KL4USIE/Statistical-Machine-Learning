import math
import random
import numpy
#Task 2a

#Function for finding the maximum likelihood for given s within x = -100...100
def findMaximum(s):	
	if s == 0:
		return "Undefined"
	values = [0]*100
	for x in range(0, 100):
		values[x] = 1/s * math.exp(-x/s)
	max_value = numpy.max(values)
	return max_value

print("Launching...")
for s in range(-40,41):
	print("Maximum of s=", s, ": ", findMaximum(s))
print("Maximum of s=", 0.001, ": ", findMaximum(0.001))