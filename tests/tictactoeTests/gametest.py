import unittest
from tictactoe.game import TicTacToe

class TicTacToeTest(unittest.TestCase):

    def setUp(self):
        self.ticTacToe = TicTacToe()

    def testInitializeGame(self):
        pass

    def test_FirstMove_picksHighestChanceOfVictory(self):
        currentBoard = ""
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
        nextMove = self.ticTacToe.nextMove(currentBoard)
        self.assertEquals("9", nextMove, "first player puts an X on bottom right box")


    def test_FirstMove_picksHighestChanceOfVictoryOrLowerChanceOfFailure(self):
        currentBoard = ""
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
        nextMove = self.ticTacToe.nextMove(currentBoard)
        self.assertEquals("3", nextMove, "first player puts an X on bottom right box")

    def test_SecondMove_picksHighestChanceOfVictoryOrLowerChanceOfFailure(self):
        currentBoard = "3"
        self.ticTacToe.moves = {
            "3": {
                "31": {"failures": 500, "victories": 1000, "draws": 2000},
                "32": {"failures": 1000, "victories": 300, "draws": 2000},
                "34": {"failures": 100, "victories": 1000, "draws": 2000},
                "35": {"failures": 500, "victories": 1000, "draws": 2000},
                "36": {"failures": 500, "victories": 1000, "draws": 2000},
                "37": {"failures": 500, "victories": 1000, "draws": 2000},
                "38": {"failures": 500, "victories": 1000, "draws": 2000},
                "39": {"failures": 200, "victories": 1000, "draws": 2000}
            }
        }

        nextMove = self.ticTacToe.nextMove(currentBoard)
        self.assertEquals("34", nextMove, "second player puts and X on top right box")

        #$TO_DO: why move 3 was not removed in moves, but move 4?

if __name__ == '__main__':
    unittest.main()