#!/usr/bin/env python

from __future__ import with_statement
import operator
import itertools


def horz_window(data, width=4):
    cols = len(data[0]) - width
    for line in data:
        for i in xrange(cols):
            yield reduce(operator.mul, line[i:i+width])

def diag_window(data, width=4):
    rows, cols = len(data) - width, len(data[0]) - width
    for i in xrange(rows):
        for j in xrange(cols):
            yield reduce(operator.mul, [ data[i+k][j+k] for k in xrange(width) ])

def adiag_window(data, width=4):
    rows, cols = len(data), len(data[0]) - width
    for i in xrange(width, rows):
        for j in xrange(cols):
            yield reduce(operator.mul, [ data[i-k][j+k] for k in xrange(width) ])

if __name__ == '__main__':

    with open("euler11.txt") as inf:
        data = [ map(int, line.split()) for line in inf ]

    print max(itertools.chain(horz_window(data), horz_window(zip(*data)), diag_window(data), adiag_window(data)))
