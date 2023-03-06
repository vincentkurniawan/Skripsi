# A game played on one board -- with mutiple wolf in that board, all parameters adjusted here.
# A game has: wolf orders

import pickle
from Model.Wolf import Wolf

class Game:
    def __init__(self, populationCount, seed, punishments, epoch) -> None:
        self.populationCount = populationCount
        self.seed = seed
        self.punishments = punishments
        self.epoch = epoch
        self.population = []
        self.getBoards()

    # input board collection from Dataset on single level
    def getBoards (self):
        inventory = pickle.load(open('Dataset2/7_easy.pkl', 'rb'))
        for board in inventory:
            self.startSearching(board)

    # start GWO algorithm on a single game, it returns the best solution found so far
    def startSearching (self, board):
        # create wolf population
        for _ in range (self.populationCount):
            self.population.append(Wolf(board, self.seed, self.punishments))

        