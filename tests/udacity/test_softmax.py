
import unittest
import numpy as np

from logic_classifier.SoftMaxEq import SoftMax

class TicTacToeTest(unittest.TestCase):

    def setUp(self):
        self.SM = SoftMax()




    def test_check1D(self):
        scores = [1.0, 2.0, 3.0]
        actual = self.SM.softmax(scores)
        #expected = np.array( [ 0.09003057,  0.24472847,  0.66524096] )
        expected = np.array([0.09003057317038046, 0.24472847105479767, 0.6652409557748219])
        print type(expected)
        print type(actual)
        self.assertEquals(type(expected) , type(actual), "actual and expeted same type")
        eL = expected.tolist()
        aL = actual.tolist()
        print eL, ' ', aL

        self.assertItemsEqual(eL, aL, "same values")

    def test_check2D(self):
        scores = [1.0, 2.0, 3.0]
        scores = np.array([[1, 2, 3, 6],
                           [2, 4, 5, 6],
                           [3, 8, 7, 6]])

        actual = self.SM.softmax(scores)
        #expected = np.array( [ 0.09003057,  0.24472847,  0.66524096] )
        expected = np.array([[ 0.09003057,  0.00242826,  0.01587624,  0.33333333],
 [ 0.24472847,  0.01794253,  0.11731043,  0.33333333],
 [ 0.66524096,  0.97962921,  0.86681333,  0.33333333]])
        print type(expected)
        print type(actual)
        self.assertEquals(type(expected) , type(actual), "actual and expeted same type")
        eL = expected.tolist()
        aL = actual.tolist()
        print eL, ' ', aL

        #self.assertItemsEqual(eL, aL, "same values")