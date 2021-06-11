import os


d = '.\dataSets\Aufgabe3'

arrayC1 = []
arrayC2 = []

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
            #Doing my best to get the data into a nice format
            lineArray[2] = lineArray[2][:-1]            
            lineArray.pop(0)
            #print(lineArray)
            if(filename.endswith("1.txt")):
                arrayC1.append(float(lineArray[0]))
                arrayC1.append(float(lineArray[1]))
            if(filename.endswith("2.txt")):
                arrayC2.append(float(lineArray[0]))
                arrayC2.append(float(lineArray[1]))

print("Listing C1: \n", arrayC1)
C1Prob = 0
C2Prob = 0
for prob in arrayC1:
    C1Prob += prob
for prob in arrayC2:
    C2Prob += prob
C1Prob /= len(arrayC1)
C2Prob /= len(arrayC1)
print("\n C1 averaged:", C1Prob, "; C2 averaged:", C2Prob)
