#!/usr/bin/env python

from itertools import *
import operator 

days = [ 31, lambda year: 29 if year % 400 or (year %4 and not year % 100) else 28, 
        30, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]

def dom(start=1900, end=2001):
    for year in xrange(start, end):
        for month_len in days:
            try:
                for d in xrange(month_len):
                    yield d == 1
            except TypeError:
                for d in xrange(month_len(year)):
                    yield d == 1

if __name__ == '__main__':
    
    print reduce(operator.add, 
            imap(operator.__and__, cycle(map(lambda x: x == 0, xrange(7))), dom())) 
    - reduce(operator.add, 
            imap(operator.__and__, cycle(map(lambda x: x == 0, xrange(7))), dom(1900,1901)))

 
