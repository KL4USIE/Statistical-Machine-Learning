import numpy as np
import matplotlib.pyplot as plt

def markovChain(s0, p, g):
    s = s0.copy()
    result = np.zeros(g+1)
    result[0]=s[0]
    for i in range(1, g+1):
        s = s.dot(p)
        result[i]=s[0]
    return result

s0 = np.array([1, 0])
s1 = np.array([0.026, 0.974])
p = np.array([[0.42, 0.58],[0.026, 0.974]])
n = np.arange(0, 19, 1)

gen18 = markovChain(s0, p, 18)
gen18prog = markovChain(s1, p, 18)

plt.plot(n, gen18, 'b')
plt.plot(n, gen18prog, 'r')
plt.xlabel('Generations')
plt.ylabel('Probability')
plt.title('Virus through the generations Task 3')
plt.grid(True)
plt.show()
