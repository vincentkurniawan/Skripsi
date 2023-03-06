# A wolf has: a board, a fitness from the board
# A wolf could do: switch board lamp position

from Model.Board import Board

class Wolf:

    def __init__(self, board, seed, punishment) -> None:
        self.board = Board(board)
        self.seed = seed
        self.punishment = punishment

    # first GWO steps
    def firstGWO (self):
        pass

    # second GWO steps
    def secondGWO (self):
        pass
    
    # a wolf could change its lamp position
    def updatePosition (self):
        pass