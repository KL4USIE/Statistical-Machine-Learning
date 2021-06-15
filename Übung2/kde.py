# Code for kde
min = -4
max = 8

def kernel(x, data, sigma):
    return (np.sum(np.exp(-(x - data) ** 2 / (2 * sigma ** 2))))
            / (np.sqrt(2 * math.pi) * len(data) * sigma)


def kde():
    sigmas = [0.03, 0.2,.8]
    x = np.arange(min, max, ((max - min) / 500))
    plt.figure()
    for sigma in sigmas:

        y = np.empty(trainingData.values.shape[0])
        for i, val in enumerate(trainingData.values):
            y[i] = kernel(val, trainingData.values, sigma)

        y = np.empty(x.shape)
        for i, val in enumerate(x):
            y[i] = kernel(val, trainingData.values, sigma)

        plt.plot(x, y, label="$\sigma=$" + str(sigma))
        plt.ylabel('Density function')
        plt.xlabel('x')

    plt.legend()
    plt.show()

kde()
