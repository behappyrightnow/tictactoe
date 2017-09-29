class TicTacToe(object):
    def __init__(self):
        self.board = ""
        self.moves = {}

    def nextMove(self, currentBoard):
        prior = "START"
        if currentBoard != '':
            self.board = currentBoard
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


