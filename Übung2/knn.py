# Code for knn
min = -4
max = 8

def knn():
    ks = [2, 8, 35]
    x = np.arange(min, max, ((max - min) / 300))

    d = cdist(x.reshape(x.shape[0], 1),
        trainingData.values.reshape(trainingData.values.shape[0], 1),
        metric="minkowski")

    for k in ks:
        y = np.empty(x.shape)
        for i, val in enumerate(d):
            V = val[np.argpartition(val, range(k))[:(k)]][-1]

            y[i] = k / (trainingData.values.shape[0] * V * 2)

        plt.plot(x, y, label="k={}".format(k))
        plt.ylabel('Density Function')
        plt.xlabel('x')

    plt.legend()
    plt.show()

knn()
