"""Softmax."""

scores = [3.0, 1.0, 0.2]

import numpy as np


def getVstack(x):
    return np.vstack([x, np.ones_like(x), 0.2 * np.ones_like(x)])


def softmax(x):
    # """Compute softmax values for each sets of scores in x."""
    # TODO: Compute and return softmax
    if (str(type(scores)) != "<type 'numpy.ndarray'>"):
        x = np.array(x)
        x = getVstack(x)
    print(x)
    counter = 0
    xps = []
    for row in x:
        counter = counter + 1
        if counter == 1:
            for elem in row:
                xps.append(np.exp(elem))

    print (type(xps))
    print (type(x[1]))
    x[1] = xps
    sumProbs = np.sum(xps)
    print(sumProbs)
    print(x)
    probs = [a / sumProbs for a in xps]
    print(probs)
    print(type(probs))
    print (type(x[2]))
    x[2] = probs
    return x[2]


print(softmax(scores))

# Plot softmax curves
import matplotlib.pyplot as plt
# x = np.arange(-2.0, 6.0, 0.1)
# x = np.arange(-1.0,2,0.1)
# scores_ = getVstack(x)
# r = softmax(scores_)
# plt.plot(x, softmax(scores).T, linewidth=2)
# plt.show()
