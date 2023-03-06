# A board is owned by a wolf

class Board:
    # Board sizes
    SIZE_LEVEL_7 = 7
    SIZE_LEVEL_10 = 10
    SIZE_LEVEL_14 = 14
    SIZE_LEVEL_25 = 25
    SIZE_DAILY = 30
    SIZE_WEEKLY = 30
    SIZE_MONTHLY = 40

    # Difficulty
    DIFF_EASY = 'easy'
    DIFF_NORMAL = 'normal'
    DIFF_HARD = 'hard'
    DIFF_DAILY = 'daily'
    DIFF_WEEKLY = 'weekly'
    DIFF_MONTHLY = 'monthly'

    def __init__(self, board) -> None:
        self.board = board
        self.dimension = 0

    # update board lamp position
    def updateBoard (self):
        pass

    # return the board
    def getBoard (self):
        pass

    # update board fitness -- basically count the board fitness
    def updateFitness (self):
        pass

    # return board fitness
    def getFitness (self):
        pass

    # put a lamp on (row, col) board position
    # return True if lamp is on the board, False if lamp not on the board
    def putSingleLamp (self):
        pass

    # count the black square with numbers for dimension on first GWO
    # after counting, updates the board dimension
    def countBlackNumber (self):
        pass

    # count the white square for dimension on second GWO
    # after counting, updates the board dimension
    def countWhites (self):
        pass

    # return board dimension
    # this method is required for Wolf to know on what dimension they used
    def getDimension (self):
        return self.dimension