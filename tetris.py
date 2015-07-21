#!/usr/bin/python

import core
import random

class Tetris:
    def __init__(self):
        self.field = [[0 for col in range(10)] for row in range(21)]
        self.nextPiece = random.choice(core.pieces.keys)
        self.newRound = True

    def step(self):
        if self.newRound: 
            for col in len(self.field[0]):
                if self.field[0][col] != 0:
                    self.gameOver()
                    return
            self.piece = self.nextPiece
            self.x = 5 - (len(core.pieces[self.piece]) + 1)/2
            self.y = 0
            self.nextPiece = random.choice(core.pieces.keys)
            self.newRound = False
        write()

    def gameOver(self)
        pass
