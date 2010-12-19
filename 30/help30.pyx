#!/usr/bin/env python
# cython: profile=True

import numpy as np

cimport numpy as np
from stdlib cimport *
from stdio cimport sprintf
import cython

cdef enum:
    DIGITS = 10 
cdef int powers[DIGITS]
cdef int i

def set_powers(n):
    cdef int i
    for i in xrange(DIGITS):
        powers[i] = i ** n

def print_powers():
    for i in xrange(DIGITS):
        print powers[i]

cpdef bool test(int n):
    cdef int rv = 0, i = 0
    cdef char digits[8]
    cdef char zero = '0'
    sprintf(digits, '%d', n)
    for i in xrange(len(digits)):
        rv += powers[digits[i] - zero]
    return rv == n

def solve():
    cdef int rv = 0
    cdef int i
    for i in range(10, 10000000):
        if test(i):
            #print i
            rv += i
    return rv 
