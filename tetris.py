#!/usr/bin/python
# -*- coding: latin-1 -*-

import os
from msvcrt import getch

from step import step
from draw import *
from core import *

ESC = 27

def getmove():
    return ord(getch())

def tetris():
    field = [[0 for col in range(10)] for row in range(20)]
    draw(field)
    while True:
        draw(field)
        key = getmove()
        if key == ESC:
            break
        else: 
            field = step(field, key)
        os.system('clear')


if __name__ == "__main__":
    draw(rotate(pieces['I']))
    tetris()

