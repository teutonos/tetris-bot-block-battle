#!/usr/bin/python
# -*- coding: latin-1 -*-

import sys
from utils import copy

def draw(field, piece, piecePos):
    s = '.OX0'
    fieldCopy = copy(field)
    for row in range(len(piece)):
        for col in range(len(piece[row])):
            fieldCopy[row+piecePos[1]][col+piecePos[0]] = 1
    for row in fieldCopy:
        for cell in row:
            sys.stdout.write('%s' % s[cell])
        sys.stdout.write('\n')
    sys.stdout.flush()