import numpy as np
import pyximport
pyximport.install()

import eratosthenes

A = np.ones(5000000, dtype='int8')
eratosthenes.sieve(A)
A.dtype = 'bool'
assert not A[41 * 41]
print np.where(A)[0]
