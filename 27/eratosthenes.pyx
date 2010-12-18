#!/usr/bin/env python
# cython: profile=True

import numpy as np

cimport numpy as np
from stdlib cimport *
import cython

def sieve(buf):
    '''
    sieve(ndarray A) -> None

    Given an ndarray (dtype bool, ndim 1) initialized to True, set to
    False all entires at composite indices.
    '''

    cdef np.ndarray[np.int8_t] A = buf
    cdef Py_ssize_t maximum = buf.shape[0]
    cdef Py_ssize_t max_index = int(np.sqrt(buf.shape[0])) + 1
    cdef Py_ssize_t i

    A[0] = A[1] = 0

    for i in xrange(2, max_index):
        if not A[i]: continue
        for j in xrange(2 * i, maximum, i):
            A[j] = 0

