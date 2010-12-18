#!/usr/bin/env python

import numpy as np
from operator import mul, itemgetter
from itertools import *
from numbers import Integral
import cProfile

def eratosthenes(block=[2, 3, 5, 7, 9, 11, 13, 17, 19], width=4):

    for b in block:
        yield b

    first = 2
    width = reduce(mul, block[:width])
    while True:
        field = np.ones(width, dtype='bool')
        block_ar = np.array(block)
        for b in block_ar[block_ar <= first]: field[ (b - (first % b)) % b :: b ] = False
        for b in block_ar[block_ar > first]: field[ b - first :: b ] = False
        #print map(lambda x: x + first, islice(ifilter(lambda x: field[x], xrange(field.shape[0])), 30))
        #return (block, first, field)
        try:
            while True:
                p = field.nonzero()[0][0] + first
                field[p - first :: p] = False
                #block.append(p)
                #print "next p is %d" % p
                yield p
        except IndexError:
            first += width

def prime_factorize(n, primes=None):
    if n < 2: 
        raise ValueError(n, 'expected n >= 2, got %s' % n)
    if not isinstance(n, Integral): 
        raise ValueError(n, 'expected integer, got %s' % n)

    if primes is None: primes = eratosthenes()
    factors = {}
    for p in primes:
        factors[p] = 0
        while not n % p:
            factors[p] +=1
            n /= p
            if n == 1:
                return dict([ (k, v) for k, v in factors.items() if v != 0])

def count_up(start=0, stop=None, incr=1):
    while stop is None or start < stop:
        yield start
        start += incr

def solve():
    n = 3
    for i in count_up(3):
        n += i
        m = reduce(mul, [ x + 1 for x in prime_factorize(n).values()])
        if m > 500:
            print n
            break;

if __name__ == '__main__':
    cProfile.run('solve()')






