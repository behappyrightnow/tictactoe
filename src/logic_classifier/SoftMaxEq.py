"""Softmax."""


import numpy as np

class SoftMax():
    def getVstack(self, x):
        return np.vstack([x, np.ones_like(x), 0.2 * np.ones_like(x)])


    def softmax(self, x):
        # """Compute softmax values for each sets of scores in x."""
        if (str(type(x)) != "<type 'numpy.ndarray'>"):
            x = np.array(x)
            x = self.getVstack(x)

        counter = 0
        xps = []
        for row in x:
            counter = counter + 1
            if counter == 1:
                for elem in row:
                    xps.append(np.exp(elem))

        x[1] = xps
        sumProbs = np.sum(xps)
        x[2] = [a / sumProbs for a in xps]
        return x[2]



if __name__ == '__main__':
    scores = [3.0, 1.0, 0.2]
    scores = [1.0, 2.0, 3.0]
    sm = SoftMax()
    print(sm.softmax(scores).T)

# Plot softmax curves

# juypeter notebook
#import matplotlib.pyplot as plt
# x = np.arange(-2.0, 6.0, 0.1)
# x = np.arange(-1.0,2,0.1)
# scores_ = self.getVstack(x)
# r = softmax(scores_)
# plt.plot(x, softmax(scores).T, linewidth=2)
# plt.show()
