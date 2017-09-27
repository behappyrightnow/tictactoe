class TicTacToe(object):
    def __init__(self, numSquares=9):
        self.board = ""
        self.moves = {}
        self.numSquares = numSquares
        # print "Building default knowledge structure..."
        self.init_moves_knowledge()
        # print "Done initializing default knowledge structure. Starting to play game."

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
                self.moves[prior] = self.null_knowledge()
                self.init_moves_knowledge(newBoard)


    def make_move(self):
        self.board = self.next_move()


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

if __name__ == '__main__':
    ticTacToe = TicTacToe()
    while len(ticTacToe.board) < 9:
        ticTacToe.make_move()
        print ticTacToe.board