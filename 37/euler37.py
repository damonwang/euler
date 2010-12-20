from os import path
import numpy as np
import pyximport
pyximport.install()

import eratosthenes

__cache__ = 'cache.npy'
__max_prime__ = int(1e6)

if path.exists(__cache__):
    primes = np.load(__cache__)
else:
    is_prime = np.ones(__max_prime__, dtype='int8')
    eratosthenes.sieve(is_prime)
    primes = np.where(is_prime)[0]

def left_truncatable(n, moduli=[ 10**(i+1) 
        for i in xrange(int(np.log10(__max_prime__))) ]):
    '''
    left_truncatable(int n) -> bool

    returns true iff every left-truncation of n is prime.
    '''

    assert n < __max_prime__, n
    for m in moduli:
        if not is_prime[ n % m ]:
            return False
    return True

def right_truncatable(n):
    '''
    right_truncatable(int n) -> bool

    returns true iff every right-truncation of n is prime.
    '''

    while n > 0:
        if not is_prime[n]: return False
        n //= 10
    return True

def solve():

    rv = filter(lambda n: right_truncatable(n) and left_truncatable(n) and n > 10,
            primes)
    assert len(rv) == 11
    return sum(rv)
    

