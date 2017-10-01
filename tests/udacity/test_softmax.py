
import unittest
import numpy as np

from logic_classifier.SoftMaxEq import SoftMax

class TicTacToeTest(unittest.TestCase):

    def setUp(self):
        self.SM = SoftMax()

    def test_check1D_uniformDistPreMultiply(self):
        scores = [3.0, 1.0, 0.2]
        scores = np.array(scores)
        actual = self.SM.softmax(scores)
        expected = np.array([0.8360188027814407, 0.11314284146556011, 0.05083835575299916] )

        self.assertEquals(type(expected) , type(actual), "actual and expeted same type")
        eL = expected.tolist()
        aL = actual.tolist()

        self.assertItemsEqual(eL, aL, "same values")

    def test_check1D_ScenarioScoresX10(self):
        scores = [3.0, 1.0, 0.2]
        FACTOR = 10
        scores= np.array(scores)
        actual = self.SM.softmax(scores * FACTOR)
        expected = np.array([0.9999999979381551, 2.0611536181887785e-09, 6.914400092683782e-13])
        self.assertEquals(type(expected) , type(actual), "actual and expeted same type")
        eL = expected.tolist()
        aL = actual.tolist()
        print '\n\nMULTIPY 10:'
        print '\n\n-->actual:', aL
        print '-->expect:', eL
        print '-->scores:', scores * FACTOR
        self.assertItemsEqual(eL, aL, "same values")

    def test_check1D_ScenarioScoresDIV10(self):
        scores = [3.0, 1.0, 0.2]
        FACTOR = 10
        scores= np.array(scores)
        actual = self.SM.softmax(scores / FACTOR)
        expected = np.array([0.3884227500459727, 0.31801365065776, 0.2935635992962673])
        self.assertEquals(type(expected) , type(actual), "actual and expeted same type")
        eL = expected.tolist()
        aL = actual.tolist()
        print '\n\nDIVIDE 10:'
        print '\n\n-->alctual:', aL
        print '-->expect:', eL
        print '-->scores:', scores / FACTOR
        self.assertItemsEqual(eL, aL, "same values")

    def test_check1D(self):
        scores = [1.0, 2.0, 3.0]
        actual = self.SM.softmax(scores)
        #expected = np.array( [ 0.09003057,  0.24472847,  0.66524096] )
        expected = np.array([0.09003057317038046, 0.24472847105479767, 0.6652409557748219])

        self.assertEquals(type(expected) , type(actual), "actual and expeted same type")
        eL = expected.tolist()
        aL = actual.tolist()
        self.assertItemsEqual(eL, aL, "same values")

    def test_check2D(self):
        scores = np.array([[1, 2, 3, 6],
                           [2, 4, 5, 6],
                           [3, 8, 7, 6]])

        actual = self.SM.softmax(scores)
        #expected = np.array( [ 0.09003057,  0.24472847,  0.66524096] )
        expected = np.array([
            [ 0.09003057,  0.00242826,  0.01587624,  0.33333333],
            [ 0.24472847,  0.01794253,  0.11731043,  0.33333333],
            [ 0.66524096,  0.97962921,  0.86681333,  0.33333333]])
        expected = np.array([
            [0.09003057317038046, 0.002428258029591337, 0.01587623997646677, 0.33333333333333337],
            [0.24472847105479767, 0.017942534803329194, 0.11731042782619837, 0.33333333333333337],
            [0.6652409557748219, 0.9796292071670795, 0.8668133321973348, 0.33333333333333337]])

        self.assertEquals(type(expected) , type(actual), "actual and expeted same type")
        eL = expected.tolist()
        aL = actual.tolist()
        self.assertItemsEqual(eL, aL, "same values")