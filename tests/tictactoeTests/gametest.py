import unittest
from tictactoe.game import TicTacToe
from smarttest import SmartTest

class MockTicTacToe(TicTacToe):
    def init_moves_knowledge(self, board=""):
        prior = board
        if prior == "":
            prior = "START"
        for i in range(1,self.numSquares+1):
            newMove = str(i)
            if newMove not in board:
                newBoard = "%s%s" % (board, newMove)
                if prior not in self.moves:
                    self.moves[prior] = {}
                self.moves[prior][newBoard] = self.null_knowledge()
                self.init_moves_knowledge(newBoard)

class TicTacToeTest(SmartTest):

    def setUp(self):
        self.ticTacToe = MockTicTacToe(numSquares=3)

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
        nextMove = self.ticTacToe.next_move()
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
        nextMove = self.ticTacToe.next_move()
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
        nextMove = self.ticTacToe.next_move()
        self.assertEquals("38", nextMove, "first player puts an X on bottom right box")

    def test_initMovesKnowledge(self):
        keysExpected = [
            "START", "1", "2", "3", "12", "13", "21", "23", "31", "32"
        ]
        keysNotExpected = [
            "11", "22", "33"
        ]
        for key in keysExpected:
            self.assertTrue(key in self.ticTacToe.moves, "%s should be in move knowledge structure" % key)

        for key in keysNotExpected:
            self.assertTrue(key not in self.ticTacToe.moves, "%s should not be in move knowledge structure" % key)
        movesAtStart = self.ticTacToe.moves["START"]
        expectedMoves = ["1", "2", "3"]
        for move in expectedMoves:
            self.assertTrue(move in movesAtStart, "should have found move %s" % move)

        expectedMoves = ["12", "13"]
        movesAt1 = self.ticTacToe.moves["1"]
        for move in expectedMoves:
            self.assertTrue(move in movesAt1, "should have found move %s" % move)

    def test_checkOutcome_Victory(self):
        self.ticTacToe.board = "1"
        self.assertEquals(self.ticTacToe.OPEN, self.ticTacToe.result(), "game is still open")
        self.ticTacToe.board = "1593748"
        self.assertEquals(self.ticTacToe.VICTORY, self.ticTacToe.result(), "this position has won")

    def test_checkOutcome_Victory_Player2(self):
        self.ticTacToe.board = "357189"
        self.assertEquals(self.ticTacToe.VICTORY, self.ticTacToe.result(), "this position has won")
        self.assertTrue(self.ticTacToe.hasWon(self.ticTacToe.PLAYER2), "player 2 should have won")

    def test_checkOutcome_Draw(self):
        self.ticTacToe.board = "375146289"
        self.assertEquals(self.ticTacToe.DRAW, self.ticTacToe.result(), "this position has drawn")

    def test_player1moves(self):
        self.ticTacToe.board = "1593748"
        self.assertEquals("1978", self.ticTacToe.movesFor(self.ticTacToe.PLAYER1), "moves for player 1")
        self.assertEquals("534", self.ticTacToe.movesFor(self.ticTacToe.PLAYER2), "moves for player 2")

    def test_availableMoves(self):
        self.ticTacToe.board = "35714"
        expected_available_moves = ["2","6","8","9"]
        self.assertEquals(expected_available_moves, self.ticTacToe.available_moves(), "available moves")

    def test_winningMove(self):
        self.ticTacToe.board = "35714"
        next_move = self.ticTacToe.next_move()
        self.assertEquals("357149", next_move, "game should be won by Player 2 at this point")
        self.assertTrue(self.ticTacToe.hasWon(self.ticTacToe.PLAYER2), "Player 2 should have won")

    def test_winningMove2(self):
        self.ticTacToe.board = "19572"
        next_move = self.ticTacToe.next_move()
        self.assertEquals("195728", next_move, "game should be won by Player 2 at this point")
        self.assertTrue(self.ticTacToe.hasWon(self.ticTacToe.PLAYER2), "Player 2 should have won")

if __name__ == '__main__':
    unittest.main()