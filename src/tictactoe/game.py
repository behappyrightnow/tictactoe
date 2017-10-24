import random

class TicTacToe(object):
    VICTORY = 0
    DRAW = 1
    OPEN = 2
    PLAYER1 = 3
    PLAYER2 = 4

    def __init__(self, numSquares=9):
        self.board = ""
        self.moves = {}
        self.numSquares = numSquares
        print "Building default knowledge structure..."
        self.init_moves_knowledge()
        print "Done initializing default knowledge structure. Starting to play game."

    def null_knowledge(self):
        return {"failures": 0, "victories": 0, "draws": 0}

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

    def hasWon(self, player):
        playerMoves = self.movesFor(player)
        winningPatterns = ["123", "147", "789", "369", "159", "357", "456", "257"]
        for winningPattern in winningPatterns:
            won = False
            for move in winningPattern:
                match = True
                if move not in playerMoves:
                    match = False
                    break
            if match:
                won = True
                break
        return won

    def gameStillOpen(self):
        return len(self.board) < 9

    def result(self):
        if self.hasWon(self.PLAYER1) or self.hasWon(self.PLAYER2):
            return self.VICTORY
        elif self.gameStillOpen():
            return self.OPEN
        else:
            return self.DRAW

    def movesFor(self,player):
        answer = ""
        for i,char in enumerate(self.board):
            if player == self.PLAYER1:
                test = i+1
            elif player == self.PLAYER2:
                test = i+2
            else:
                raise "Unrecognized input for player %s" % (str(player))
            if test % 2 != 0:
                answer = "%s%s" % (answer, char)
        return answer

    def make_move(self):
        self.board = self.next_move()

    def make_random_move(self):
        available_moves = ['1','2','3','4','5','6','7','8','9']
        for move in self.board:
            available_moves.remove(move)
        randomMoveIndex = random.randrange(start=0, stop=len(available_moves))
        self.board = "%s%s" % (self.board,available_moves[randomMoveIndex])

    def next_move(self):
        prior = "START"
        if self.board != "":
            prior = self.board

        bestMove = None
        bestMoveID = None
        moveData = self.moves[prior]
        for moveID in moveData:
            move = moveData[moveID]
            if bestMove == None:
                bestMove = move
                bestMoveID = moveID
            else:
                if move["victories"] > bestMove["victories"]:
                    bestMove = move
                    bestMoveID = moveID
                elif move["failures"] < bestMove["failures"]:
                    bestMove = move
                    bestMoveID = moveID
                elif move["draws"] > bestMove["draws"]:
                    bestMove = move
                    bestMoveID = moveID
        return bestMoveID

    def start_learning(self, numGames=100):
        for i in range(1,100):
            print "Playing game %s" % i
            print self.play_game()

    def play_game(self):
        ticTacToe.board = ""
        while len(ticTacToe.board) < 9 and ticTacToe.result() == ticTacToe.OPEN:
            ticTacToe.make_random_move()
            print ticTacToe.board
        if ticTacToe.result() == ticTacToe.VICTORY:
            if ticTacToe.hasWon(ticTacToe.PLAYER1):
                winner = "Player 1"
            else:
                winner = "Player 2"
            return "The game ended in a victory for %s." % winner
        elif ticTacToe.result() == ticTacToe.DRAW:
            print "The game ended in a draw."
        self.learn()

    def learn(self):
        #TODO: Go through each move and learn from it
        pass

if __name__ == '__main__':
    ticTacToe = TicTacToe(numSquares=9)
    print ticTacToe.start_learning()

