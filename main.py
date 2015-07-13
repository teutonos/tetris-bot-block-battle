#!/usr/bin/python
# -*- coding: latin-1 -*-

import sys

from tetris import core

def fitness(score, combo, field):
    return 0

def bot():
    while not sys.stdin.closed:
        try:
            rawline = sys.stdin.readline()
            # End of file check
            if len(rawline) == 0:
                break
            line = rawline.strip()
            # Empty lines can be ignored
            if len(line) == 0:
                continue
            parts = line.split()
            command = parts[0]
            if command == 'settings':
                pass
            elif command == 'update':
                pass
            elif command == 'action':
                sys.stdout.write('drop\n')
                sys.stdout.flush()
        except EOFError:
            return

if __name__ == "__main__":
    bot()