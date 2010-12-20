from collections import defaultdict
from itertools import count
from operator import itemgetter
from math import sqrt, ceil
import unittest

'''
Euclid's formula for Pythagorean triples is
    a = m^2 - n^2
    b = 2mn
    c = m^2 + n^2
where 
    m, n positive integers and m > n
This generates all primitive triples uniquely (but not only primitive
triples). Multiplying by a positive integer coefficient k:
    a = k * (m^2 - n^2)
    b = k * (2mn)
    c = k * (m^2 + n^2)
generates all triples, but not uniquely. So,
    p = a + b + c = k * ( 2m^2 + 2mn )
For any P, when
    2m > 1 + sqrt(1 + 2P)
no positive value of n or k will satisfy p < P.
'''

__max_perimeter__ = 1000

def solve():
    triples = set()
    bound = int(ceil(.5 * 1 + sqrt(1 + 2*__max_perimeter__)))
    for m in xrange(1, bound):
        for n in xrange(1, m):
            a, b, c = m*m - n*n, 2*m*n, m*m + n*n
            p = a + b + c
            if p > __max_perimeter__: break
            for k in count(1):
                if k * p > __max_perimeter__: break
                triples.add((k * a, k * b, k * c))
    multiplicities = defaultdict(lambda : 0)
    for a, b, c in triples:
        multiplicities[ a + b + c ] += 1
    return max(multiplicities.items(), key=itemgetter(1))[0]
                
class TestSolve(unittest.TestCase):

    def test_solve(self):
        self.assert_(solve() == 840)

def run_tests(verbosity=0, tests=[]):
    tests = [ unittest.TestLoader().loadTestsFromTestCase(v)
            for k,v in globals().items()
            if k.startswith("Test") and (tests == [] or k in tests)]
    unittest.TextTestRunner(verbosity=verbosity).run(unittest.TestSuite(tests))

if __name__ == '__main__':

    run_tests()
