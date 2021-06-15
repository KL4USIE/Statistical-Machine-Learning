# Code for histogram
trainingData = p.read_csv("nonParamTrain.txt", sep="\s{2}")
testData = p.read_csv("nonParamTest.txt", sep="\s{2}")
trainingData.columns = testData.columns = ["value"]


def histo():
    size = [0.02, 0.5, 2.0]

    for i, s in enumerate(size):
        plt.figure(i)
        trainingData.plot.hist(by="value", bins=math.ceil(trainingData.max().value / s))
        plt.xlabel("x")
        plt.title("Histogram {}".format(s))

histo()
plt.show()
