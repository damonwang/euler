#!/usr/bin/env python
# cython: profile=True

import numpy as np

cimport numpy as np
from stdlib cimport *
import cython

def fibonacci(out):
    '''
    fibonacci(ndarray[np.int64_t, ndim=1] out) -> None

    fills in `out` with the Fibonacci sequence, starting with
        out[0] = 0
        out[1] = 1
    '''

    assert out.ndim == 1

    cdef np.ndarray[np.int64_t] F = out
    cdef Py_ssize_t length = out.shape[0]
    cdef Py_ssize_t i

    F[0], F[1] = 0, 1

    for i in range(2, length):
        F[i] = F[i-1] + F[i-2]
