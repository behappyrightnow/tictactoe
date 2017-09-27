'''
Created on Dec 27, 2011

@author: sraha
'''
import unittest
import math


class SmartTest(unittest.TestCase):

    def assertDictEquals(self, expected, actual, message, places=2):
        if (type(expected) is dict):
            for key in expected:
                expectedValue = expected[key]
                if key not in actual:
                    self.fail(message+ " did not find key '%s' in actual" % key)
                actualValue = actual[key]
                if type(expectedValue) is str:
                    self.assertStringEquals(expectedValue, actualValue, message+", checking key '%s' " % key)
                elif type(expectedValue) is dict:
                    self.assertDictEquals(expectedValue, actualValue, message+"\n\t, checking key '%s' " % key, places)
                elif type(expectedValue) is list:
                    self.assertArrayEquals(expectedValue, actualValue, message+"\n\t checking key '%s'" % key, places)
                elif expectedValue == None:
                    self.assertNone(actualValue, message+"\n\t checking key '%s'" % key)
                else:
                    self.assertNumberEquals(expectedValue, actualValue, message+", checking key '%s' " % key, places)

    def assertNone(self, actual, message):
        if actual != None:
            self.fail(message+", expected None but got %s" % str(actual))

    def assertArrayEquals(self, expected, actual, message, places=2):
        counter = 0
        for expectedItem in expected:
            if counter >= len(actual):
                self.fail("Expected %s but actual array did not have any more elements.\nFull Expected Array: %s\nFull Actual Array: %s" % (expectedItem, expected, actual))
            actualItem = actual[counter]
            if type(expectedItem) is str or type(expectedItem) is unicode:
                self.assertStringEquals(expectedItem, actualItem, message+" item %s: expected '%s' but was '%s'" % (str(counter),expectedItem, actualItem))
            elif type(expectedItem) is dict:
                self.assertDictEquals(expectedItem, actualItem, message, places)
            elif type(expectedItem) is list:
                self.assertArrayEquals(expectedItem, actualItem, message+" Entering list in array[%s], expected\n\t %s\n but got\n\t %s)" % (str(counter), str(expectedItem), str(actualItem)), places)
            else:
                self.assertNumberEquals(expectedItem, actualItem, " item %s\n\t expected\n\t\t '%s'\n but was\n\t\t '%s'" % (str(counter),str(expectedItem), str(actualItem)), places)
            counter = counter + 1
        unittest.TestCase.assertEquals(self,len(expected), len(actual), message+" number of items expected '%s' but was '%s'" % (str(len(expected)), str(len(actual))))

    def assertEquals(self, expected, actual, message,places=2):
        if type(expected) is list:
            self.assertArrayEquals(expected, actual, message, places)
        elif type(expected) is dict:
            self.assertDictEquals(expected, actual, message, places)
        elif expected == None:
            self.assertNone(actual, message)
        else:
            if type(expected) is str or type(expected) is unicode:
                self.assertStringEquals(expected, actual, "\nexpected:\n\t '%s'\nbut was:\n\t '%s'\n\ncontext: %s" % (expected, actual, message))
            elif expected is None:
                self.assertNoneEquals(expected, actual, "None type check")
            else:
                self.assertNumberEquals(expected, actual, "\nexpected:\n\t '%s'\nbut was:\n\t '%s'\n\ncontext: %s" % (expected, actual, message), places)

    def assertEqual(self, expected, actual, message):
        unittest.TestCase.assertEqual(self, expected, actual, message+" expected '%s' but was '%s'" % (str(expected), str(actual)))

    def assertNumberEquals(self, expected, actual, message, places=2):
        if abs(expected - actual)>(1.0/math.pow(10,places)):
            self.fail("%s: Number mismatch. Expected %s but got %s" % (message, str(expected), str(actual)))

    def assertNoneEquals(self, expected, actual, message):
        if actual != None:
            self.fail("%s: Expect to be None but got %s" % (message, str(actual)))

    def assertStringEquals(self, expected, actual, message):
        stringComparator = StringComparator()
        msg = stringComparator.compare(expected, actual, message)
        if msg != None:
            self.fail(msg)

class StringComparator:
    def compare(self, expected, actual, message):
        errorMessage = None
        for i in range(len(expected)):
            if i < len(actual) and expected[i]!=actual[i]:
                backChars = min(20,i)
                forwardCharsExp = min(20,len(expected)-i)
                forwardCharsAct = min(20, len(actual) -i)
                expectedSome = expected[i-backChars:i+forwardCharsExp]
                cursor = " "*backChars + "^"
                actualSome = actual[i-backChars:i+forwardCharsAct]
                preview = "comparing\n%s\n%s\nwith\n%s\n%s\n" % (expectedSome, cursor,actualSome, cursor)
                errorMessage = "%s: Mismatch in character %s when %s<===EXPECTED\n'%s'\n==>\nwith\n<===ACTUAL\n'%s'\n==>" % (message, str(i), preview, expected, actual)
            elif i == len(actual):
                errorMessage = "%s: expected string %s has more characters than actual string %s" % (message, expected, actual)
        if len(actual) > len(expected) and errorMessage == None:
            errorMessage = "%s: expected string %s has fewer characters than actual string %s" % (message, expected, actual)
        return errorMessage

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()