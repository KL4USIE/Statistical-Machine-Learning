import os
import math 
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
from scipy.interpolate import griddata

d = '.\dataSets\Aufgabe3'

arrayC1 = []
arrayC2 = []
C1Prob = 0
C2Prob = 0
C1Weights = []
C2Weights = []

#Reads files, saves them in the above variables
def ReadFiles():
    print("Launching...")
    for filename in os.listdir(d):
        if not filename.endswith('.txt'):
            continue
        filename = d+"\\"+filename;
        with open(filename, 'r') as f:
            for line in f.readlines():
                #Results in an array with three elements, first is just empty, second is the first value, third is the second value+\n        
                lineArray = line.split('  ') 
                #print(lineArray)
                #So we do some formatting to clean up the mess
                lineArray[2] = lineArray[2][:-1]            
                lineArray.pop(0)
                #print(lineArray)
                if(filename.endswith("1.txt")):
                    arrayC1.append(float(lineArray[0]))
                    arrayC1.append(float(lineArray[1]))
                if(filename.endswith("2.txt")):
                    arrayC2.append(float(lineArray[0]))
                    arrayC2.append(float(lineArray[1]))
    #print("Listing C1: \n", arrayC1)   
    
def CalcMean(data):
    total = 0
    entryCount = 0
    for entry in data:
        total += entry
        entryCount += 1
    return total / entryCount

#https://www.khanacademy.org/m  ath/statistics-probability/summarizing-quantitative-data/variance-standard-deviation-population/a/calculating-standard-deviation-step-by-step
def CalcDeviation(data, mean):
    distArray = []
    distTotal = 0
    for entry in data:
        distTotal += pow(mean - entry, 2)
    final = math.sqrt(distTotal / len(data))
    return final

def CalcLikelihood(x, mean, deviation):
    r1 = 1/math.sqrt(2*math.pi*pow(deviation, 2))
    #print(r1)
    r2 = -pow(x-mean, 2)
    r2 = -pow(x, 2) +2*mean*x -pow(mean,2)
    #print(r2)
    r3 = 2*pow(deviation, 2)
    #print(r3)
    result = r1 * pow(math.e, r2/r3)
    return result

def CalcMaxLikelihood(data, mean, deviation):
    result = 0.0
    for entry in data:
        result += CalcLikelihood(entry, mean, deviation)
    return result

ReadFiles()
#for prob in arrayC1:
#        C1Prob += prob
#for prob in arrayC2:
#    C2Prob += prob
#C1Prob /= len(arrayC1)
#C2Prob /= len(arrayC2)
print("Size C1: ", len(arrayC1))
print("Size C2: ", len(arrayC2))
totalEntries = len(arrayC1) + len(arrayC2)
C1Prior = len(arrayC1) / totalEntries
C2Prior = len(arrayC2) / totalEntries
print("\n C1 prior:", C1Prior, "; C2 prior:", C2Prior)

#http://jrmeyer.github.io/machinelearning/2017/08/18/mle.html#:~:text=When%20using%20Maximum%20Likelihood%20Estimation,standard%20deviation%20of%20the%20data.
C1Mean = CalcMean(arrayC1)
C2Mean = CalcMean(arrayC2)
print("\n C1 mean:", C1Mean, "; C2 mean:", C2Mean)
C1Deviation = CalcDeviation(arrayC1, C1Mean)
C2Deviation = CalcDeviation(arrayC2, C2Mean)
print("\n C1 deviation:", C1Deviation, "; C2 deviation:", C2Deviation)
print("TESTRESULT: ", CalcLikelihood(5, C1Mean, C1Deviation))
C1MaxLikelihood = CalcMaxLikelihood(arrayC1, C1Mean, C1Deviation)
C2MaxLikelihood = CalcMaxLikelihood(arrayC2, C2Mean, C2Deviation)
print("\n C1 MaxLikelihood:", C1MaxLikelihood, "; C2 MaxLikelihood:", C2MaxLikelihood)

for entry in arrayC1:
    C1Weights.append(CalcLikelihood(entry, C1Mean, C1Deviation))
for entry in arrayC2:
    C2Weights.append(CalcLikelihood(entry, C2Mean, C2Deviation))
