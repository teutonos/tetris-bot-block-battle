#!/usr/bin/python

import core
import random

fieldSize = [10, 21]

class Tetris:
    def __init__(self):
        self.field = [
                        [0 for col in range(fieldSize[0])] 
                            for row in range(fieldSize[1])
                     ]
        self.nextPiece = random.choice(core.pieces.keys)
        self.newRound = True

    def step(self):
        if self.newRound: 
            for col in range(len(self.field[0])):
                if self.field[0][col] != 0:
                    self.gameOver()
                    return
            self.piece = core.pieces[self.nextPiece]
            self.piecePos = [(fieldSize[0] - len(self.piece))//2, 0]
            self.nextPiece = random.choice(core.pieces.keys)
            self.newRound = False
        draw(self.field, self.piece, self.piecePos)

    def gameOver(self)
        pass
