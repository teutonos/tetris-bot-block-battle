#!/usr/bin/python
# -*- coding: latin-1 -*-

from core import *
from draw import *

DOWN = 56
LEFT = 52
RIGHT = 54
TURNL = 55
TURNR = 57
DROP = 53

def copy(field):
    return [row[:] for row in field]

def step(field, move):
    if move == DOWN:
        return down(field)
    if move == LEFT:
        return left(field)
    if move == RIGHT:
        return right(field)
    if move == TURNL:
        return turnl(field)
    if move == TURNR:
        return turnr(field)
    if move == DROP:
        return drop(field)
    return

def down(field):
    fieldCopy = copy(field)
    for row in tuple(reversed(range(len(field)))):
        for col in range(len(field[row])):
            if (field[row][col] == 1):
                if row == len(field) - 1:
                    return drop(field)
                fieldCopy[row][col] = 0
                fieldCopy[row+1][col] = 1
    return fieldCopy

def left(field):
    fieldCopy = copy(field)
    for row in range(len(field)):
        for col in range(len(field[row])):
            if (field[row][col] == 1):
                if col == 0:
                    return down(field)
                fieldCopy[row][col] = 0
                fieldCopy[row][col-1] = 1
    return fieldCopy

def right(field):
    fieldCopy = copy(field)
    for row in range(len(field)):
        for col in tuple(reversed(range(len(field[row])))):
            if (field[row][col] == 1):
                if col == len(field[row]) - 1:
                    return down(field)
                fieldCopy[row][col] = 0
                fieldCopy[row][col+1] = 1
    return fieldCopy

def turnl(field):
    fieldCopy = copy(field) 
    for row in range(len(fieldCopy)):
        for col in range(len(fieldCopy[row])):
            if (fieldCopy[row][col] == 1):
                fieldCopy[row][col] = 0
    p,r = detectPiece(field)
    return fieldCopy

def detectPiece(field):
    piece = copy(field)
    for row in range(len(piece)):
        for col in range(len(piece[row])):
            if (piece[row][col] > 1):
                piece[row][col] = 0

    p = findPiece(piece)
    if p is None:
        return None

    ref = copy(pieces[p[0]])
    for i in range(p[1]):
        ref = rotate(ref)

    return diff(offset(piece), offset(ref)) + (p)

def findPiece(piece):
    stripped = strip(piece)
    for p in pieces.keys():
        tmp = copy(pieces[p])
        for i in range(4):
            if (strip(tmp) == stripped):
                return [p,i]
            tmp = rotate(tmp)
    return None

def strip(piece):
    return zip(*[row for row in 
        zip(*[row for row in piece if sum(row) > 0]) 
        if sum(row) > 0])

def offset(piece):
    for row in range(len(piece)):
        for col in range(len(piece[row])):
            if(piece[row][col] == 1):
                return [row,col]

def diff(list1, list2):
    return [a - b for a, b in zip(list1, list2)]
