#Code for exception maximization
k = 4

def em():

    covar = np.array(
        [np.identity(data.shape[1]) for _ in range(k)])
    mu = np.random.uniform(data.min().min(), data.max().max(),
                           size=(k, data.shape[1]))
    pi = np.random.uniform(size=(k,))
    likelihood = np.empty((30,))

    for i in range(30):
        alpha = e( covar, pi, mu, data.values)
        mu, covar, pi = m(data.values, alpha)

        if i + 1 in [1, 3, 5, 10, 30]:
            plt.figure(i)
            vis(data.values, i, mu, covar)
        likelihood[i] = logLikelihood(data.values, mu, covar, pi)

def m(x, alpha):
    N = np.sum(alpha, axis=1)

    m = np.zeros((k, x.shape[1]))
    c = np.zeros((k, x.shape[1], x.shape[1]))

    for i in range(k):
        for j, val in enumerate(x):
            m[i] += (alpha[i, j] * val)
        m[i] /= N[i]
        for j, val in enumerate(x):
            c[i] += alpha[i, j] * np.outer(val - m[i], (val - m[i]).T)
        c[i] /= N[i]
    pi = N / x.shape[0]

    return m, c, pi

def e(c, pi, m, x):
    alpha = np.empty((k, x.shape[0]))
    for i in range(k):
        alpha[i] = pi[i] * gaussian(x, m[i], c[i])

    return alpha / np.sum(alpha, axis=0)

def gaussian(data, m, c):
    res = np.empty(data.shape[0])
    for i, x in enumerate(data):
        diff = x - m
        res[i] = np.exp(-.5 * diff.T.dot(np.linalg.inv(c)).dot(diff)) \
        / np.sqrt((2 * math.pi) ** data.shape[1] * np.linalg.det(c))

    return res

def logLikelihood(x, m, c, pi):
    logLikelihood = np.empty((k, x.shape[0]))
    for i in range(k):
        logLikelihood[i] = pi[i] * gaussian(x, m[i], c[i])

    return np.sum(np.log(np.sum(logLikelihood, axis=0)))

def vis(data, iteration, m, c):
    x = np.arange(data[:, 0].min() - 1, data[:, 0].max() + 1,
        (data[:, 0].max() - data[:, 0].min() + 2) / 100)
    y = np.arange(data[:, 1].min() - 1, data[:, 1].max() + 1,
        (data[:, 1].max() - data[:, 1].min() + 2) / 100)
    Y, X = np.meshgrid(y, x)
    Z = np.empty((100, 100))

    for i in range(k):
        for j in range(100):
            points = np.append(X[j], Y[j]).reshape(2, x.shape[0]).T
            Z[j] = gaussian(points, m[i], c[i])
em()
