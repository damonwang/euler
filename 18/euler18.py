#!/usr/bin/env python

from __future__ import with_statement

if __name__ == '__main__':

    with open('euler18.txt') as inf:
        data = [ map(int, line.split()) for line in inf]

    with open('log.txt', 'w') as outf:
        for i in xrange(len(data) - 2, -1, -1):
            for line in data:
                print >> outf, line
            for j in xrange(len(data[i])):
                data[i][j] += max(data[i+1][j], data[i+1][j+1])

    print data[0][0]

