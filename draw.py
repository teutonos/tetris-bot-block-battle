#!/usr/bin/python
# -*- coding: latin-1 -*-

import sys

def draw(field):
    s = '.OX0'
    for row in field:
        for cell in row:
            sys.stdout.write('%s' % s[cell])
        sys.stdout.write('\n')
    sys.stdout.flush()