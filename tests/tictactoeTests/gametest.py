import unittest
from tictactoe.game import TicTacToe
from smarttest import SmartTest

class TicTacToeTest(SmartTest):

    def setUp(self):
        self.ticTacToe = TicTacToe()

    def testInitializeGame(self):
        pass

    def test_FirstMove_picksHighestChanceOfVictory(self):
        self.ticTacToe.board = ""
        self.ticTacToe.moves = {
            "START": {
                "1": {"failures": 500, "victories": 1000, "draws": 2000},
                "2": {"failures": 1000, "victories": 300, "draws": 2000},
                "3": {"failures": 500, "victories": 1000, "draws": 2000},
                "4": {"failures": 500, "victories": 1000, "draws": 2000},
                "5": {"failures": 500, "victories": 1000, "draws": 2000},
                "6": {"failures": 500, "victories": 1000, "draws": 2000},
                "7": {"failures": 500, "victories": 1000, "draws": 2000},
                "8": {"failures": 500, "victories": 1000, "draws": 2000},
                "9": {"failures": 200, "victories": 8000, "draws": 2000}
            }
        }
        nextMove = self.ticTacToe.nextMove()
        self.assertEquals("9", nextMove, "first player puts an X on bottom right box")


    def test_FirstMove_picksHighestChanceOfVictoryOrLowerChanceOfFailure(self):
        self.ticTacToe.board = ""
        self.ticTacToe.moves = {
            "START": {
                "1": {"failures": 500, "victories": 1000, "draws": 2000},
                "2": {"failures": 1000, "victories": 300, "draws": 2000},
                "3": {"failures": 100, "victories": 1000, "draws": 2000},
                "4": {"failures": 500, "victories": 1000, "draws": 2000},
                "5": {"failures": 500, "victories": 1000, "draws": 2000},
                "6": {"failures": 500, "victories": 1000, "draws": 2000},
                "7": {"failures": 500, "victories": 1000, "draws": 2000},
                "8": {"failures": 500, "victories": 1000, "draws": 2000},
                "9": {"failures": 200, "victories": 1000, "draws": 2000}
            }
        }
        nextMove = self.ticTacToe.nextMove()
        self.assertEquals("3", nextMove, "first player puts an X on bottom right box")

    def test_SecondMove_picksHighestChanceOfVictoryOrLowerChanceOfFailure(self):
        self.ticTacToe.board = "3"
        self.ticTacToe.moves = {
            "3": {
                "31": {"failures": 500, "victories": 1000, "draws": 2000},
                "32": {"failures": 1000, "victories": 300, "draws": 2000},
                "34": {"failures": 300, "victories": 1000, "draws": 2000},
                "35": {"failures": 500, "victories": 1000, "draws": 2000},
                "36": {"failures": 500, "victories": 1000, "draws": 2000},
                "37": {"failures": 500, "victories": 1000, "draws": 2000},
                "38": {"failures": 200, "victories": 1000, "draws": 3000},
                "39": {"failures": 200, "victories": 1000, "draws": 2000}
            }
        }
        #TODO: Build this testcase for second move
        nextMove = self.ticTacToe.nextMove()
        self.assertEquals("38", nextMove, "first player puts an X on bottom right box")

if __name__ == '__main__':
    unittest.main()