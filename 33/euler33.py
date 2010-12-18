import unittest 
from operator import mul, itemgetter
from euler12 import prime_factorize


def cancel(num, denom, mul=mul, primes=[2, 3, 5, 7, 11, 13, 17,
    19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89,
    97]):
    '''
    cancel(int num, int denom) -> (int, int)

    returns a lowest-common-terms representation of the rational number
        num/denom
    '''

    if num == 1 or denom == 1: return num, denom
    num_fac = prime_factorize(num, primes=primes)
    denom_fac = prime_factorize(denom, primes=primes)

    for p in num_fac:
        if p in denom_fac:
            common = min(num_fac[p], denom_fac[p])
            num_fac[p] -= common
            denom_fac[p] -= common
    
    num = reduce(mul, 
            [b ** p for b, p in num_fac.items() if p > 0 ] + [1])
    denom = reduce(mul, 
            [b ** p for b, p in denom_fac.items() if p > 0 ] + [1])

    return num, denom

def odd_cancel(num, denom):
    '''
    odd_cancel(list num, list denom) -> (list, list)

    If an element occurs in both sequences, removes it from both. This
    is like canceling in that, e.g, odd_cancel('AAB', 'ABC') -> 'A', 'C'

    Ordering of the remaining elements is preserved.
    '''

    rv = []
    for n in num:
        try: denom.remove(n)
        except ValueError: rv.append(n)
    return rv, denom

def solve(maxnum=100, maxdenom=100):
    '''
    assume that the problem requires some cancelling: e.g., 11/23
    doesn't count.

    I chose to test equality of fractions by requiring equality of both
    numerator and denominator, rather than, say, converting to float and
    risking some kind of rounding error. Probably not a big deal either
    way, though.
    '''

    rv = []

    for n in range(1, maxnum):
        for d in range(n+1, maxdenom):
            if not n % 10 and not d % 10: continue # 20/30 is trivial
            normal = cancel(n, d)
            if normal == (n, d): continue # see assumption in docstring
            odd = tuple(int(''.join(elt or ['1'])) 
                    for elt in odd_cancel(list(str(n)), list(str(d))))
            if odd == (n, d): continue # see assumption in docstring
            try: low_odd = cancel(*odd)
            except ValueError: continue
            if low_odd == normal: 
                #print n, d, normal, odd, low_odd
                rv.append(normal)

    # product of the four special fractions, in lowest terms
    num, denom = cancel(*map(lambda seq: reduce(mul, seq), zip(*rv)))
    return denom

class TestCancel(unittest.TestCase):

    def test_null(self):
        "empty denominator or numerator"

        self.assert_(cancel(10, 5) == (2, 1))
        self.assert_(cancel(5, 10) == (1, 2))
        self.assert_(cancel(5, 5) == (1, 1))

    def test_repeated(self):
        "repeated factors"

        self.assert_(cancel(125, 50) == (5, 2))
        self.assert_(cancel(50, 125) == (2, 5))

    def test_one(self):
        "ones in num or denom"

        self.assert_(cancel(1, 10) == (1, 10))
        self.assert_(cancel(10, 1) == (10, 1))

class TestOddCancel(unittest.TestCase):
    
    def test_repeat(self):
        "(ABC, AA) -> (BC, A)"

        self.assert_(odd_cancel([1, 2, 3], [1, 1]) == ([2, 3], [1]))
        self.assert_(odd_cancel([1, 1, 2], [1, 3]) == ([1, 2], [3]))

    def test_empty(self):
        "(A, A) -> (, )"

        self.assert_(odd_cancel([1], [1]) == ([], []))
        self.assert_(odd_cancel([1, 2, 3], [1, 2]) == ([3], []))

    def test_order(self):
        "(ABC, BAD) -> (C, D)"

        self.assert_(odd_cancel([1, 2, 3], [2, 1, 4]) == ([3], [4]))


def run_tests(verbosity=0, tests=[]):
    tests = [ unittest.TestLoader().loadTestsFromTestCase(v)
            for k,v in globals().items()
            if k.startswith("Test") and (tests == [] or k in tests)]
    unittest.TextTestRunner(verbosity=verbosity).run(unittest.TestSuite(tests))

if __name__ == '__main__':

    run_tests()
