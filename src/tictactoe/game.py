import random
import json
import pickle

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
        with open("/Users/Raha/PycharmProjects/tictactoe/learning/ticTacToe.pickle", "r") as f:
            self.moves = pickle.load(f)



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

    def available_moves(self):
        availableMoves = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        for move in self.board:
            availableMoves.remove(move)
        return availableMoves

    def next_move_that_wins_or_only_move(self):
        origBoard = self.board
        availableMoves = self.available_moves()
        if len(availableMoves) == 1:
            return availableMoves[0]
        for move in availableMoves:
            self.board = "%s%s" % (origBoard, move)
            if self.result() == self.VICTORY:
                self.board = origBoard
                return move
        return None

    def next_move(self):
        prior = "START"
        if self.board != "":
            prior = self.board

        winningMove = self.next_move_that_wins_or_only_move()
        if winningMove != None:
            self.board = "%s%s" % (self.board, winningMove)
            return self.board
        bestMove = None
        bestMoveID = None
        if prior in self.moves:
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
        else:
            raise "Database empty for this"
        return bestMoveID

    def start_learning(self, numGames=100):
        blockSize = int(numGames / 10)
        for i in range(1,numGames):
            # print "Playing game %s" % i
            self.play_game()
            if i % blockSize == 0:
                print "%s percent complete" % str(i*10/blockSize)

    def play_game(self):
        ticTacToe.board = ""
        resultMsg = ""
        while ticTacToe.result() == ticTacToe.OPEN:
            ticTacToe.make_random_move()
            # print ticTacToe.board
        if ticTacToe.result() == ticTacToe.VICTORY:
            if ticTacToe.hasWon(ticTacToe.PLAYER1):
                winner = "Player 1"
            else:
                winner = "Player 2"
            resultMsg = "The game ended in a victory for %s." % winner
        elif ticTacToe.result() == ticTacToe.DRAW:
            resultMsg = "The game ended in a draw."
        self.learn()
        return resultMsg

    def learn(self):
        prior = "START"

        for index, move in enumerate(self.board):
            if index % 2 == 0: #PLAYER 1
                player = self.PLAYER1
                otherPlayer = self.PLAYER2
            else:
                player = self.PLAYER2
                otherPlayer = self.PLAYER1

            nextMove = self.setupLearningStructure(move, prior)
            if self.hasWon(player):
                self.moves[prior][nextMove]["victories"] += 1
            elif self.hasWon(otherPlayer):
                self.moves[prior][nextMove]["failures"] += 1
            else:
                self.moves[prior][nextMove]["draws"] += 1
            if prior == "START":
                prior = move
            else:
                prior = nextMove

    def setupLearningStructure(self, move, prior):
        if prior not in self.moves:
            self.moves[prior] = {}
        if prior == "START":
            nextMove = move
        else:
            nextMove = "%s%s" % (prior, move)
        if nextMove not in self.moves[prior]:
            self.moves[prior][nextMove] = {"victories": 0, "failures": 0, "draws": 0}
        return nextMove


if __name__ == '__main__':
    ticTacToe = TicTacToe(numSquares=9)
    print "Playing 10 million games to learn"
    # ticTacToe.start_learning(numGames=10000000)
    # with open("/Users/Raha/PycharmProjects/tictactoe/ticTacToe.pickle", "wb") as f:
    #     pickle.dump(ticTacToe.moves, f)
    print json.dumps(ticTacToe.moves["START"], indent=4)
    #Run game with user on keyboard
    print "Let's play some Tic Tac Toe"
    whichPlayer = ""
    while whichPlayer != "X" and whichPlayer != "0":
        whichPlayer = raw_input("Which player are you? [X or 0]  ")
    ticTacToe.board = ""
    if whichPlayer == "X":
        availableMoves = ["1","2","3","4","5","6","7","8","9"]
        while ticTacToe.result() == ticTacToe.OPEN:
            for move in ticTacToe.board:
                if move in availableMoves:
                    availableMoves.remove(move)
            prompt = ""
            for index, move in enumerate(availableMoves):
                if index == 1:
                    prompt = move
                else:
                    prompt = "%s,%s" % (prompt, move)
            move = raw_input("Your move: [prompt]  ")
            ticTacToe.board = "%s%s" % (ticTacToe.board, move)
            if len(ticTacToe.board) != 9:
                ticTacToe.make_move()
                print "I moved. The board is now: %s" % ticTacToe.board
        if ticTacToe.result() == ticTacToe.VICTORY:
            if ticTacToe.hasWon(ticTacToe.PLAYER1):
                winner = "you"
            else:
                winner = "me"
            resultMsg = "The game ended in a victory for %s." % winner
        elif ticTacToe.result() == ticTacToe.DRAW:
            resultMsg = "The game ended in a draw."
        print resultMsg