import operator 
import itertools 
import unittest

def arith_sum(a, d, n):
    '''
    arith_sum(float a, float d, int n) -> float

    returns the sum of the first n terms of the sequence
        a[n] = a + (n-1)*d
    (i.e., the one-indexed arithmetic sequence from a with increment d)

    returns zero if `n` is not positive.
    '''

    return n*a + n*(n-1)*d/2 if n > 0 else 0

def solve(divisors=[3, 5], n=1000, arith_sum=arith_sum):
    '''
    solve([int] divisors=[3, 5], int n=1000) -> int

    Uses inclusion-exclusion (a.k.a., sieve) principle to return the sum
    of all positive integers less than `n` which are divisible by at
    least one of `divisors`.
    '''

    rv = 0

    divisors = map(abs, divisors)

    for i in xrange(len(divisors)):
        for I in itertools.combinations(divisors, i + 1):
            p = reduce(operator.mul, I)
            rv += (-1 if i % 2 else 1) * arith_sum(p, p, n/p - bool(not n % p))

    return rv

class TestArithSum(unittest.TestCase):
    def test_null(self):
        "sum of null sequence"

        self.assert_(arith_sum(1, 1, 0) == 0)

    def test_neg(self):
        "sum of negative-length sequence"

        self.assert_(arith_sum(1, 1, -1) == 0)

    def test_zero(self):
        "sum of one-elt sequence"

        self.assert_(arith_sum(1, 2, 1) == 1)

    def test_one(self):
        "sum of two-elt sequence"

        self.assert_(arith_sum(1, 2, 2) == 4)

class TestSolve(unittest.TestCase):

    def test_no_divisors(self):
        "empty divisors list"

        self.assert_(solve(divisors=[]) == 0)

    def test_divisors_one(self):
        "divisors = [1]"

        self.assert_(solve(divisors=[1], n=4) == 6)

    def test_divisors_neg(self):
        "negative divisors"

        self.assert_(solve(divisors=[-2], n=5) == 6)
        self.assert_(solve(divisors=[-3, 5], n=10) == 23)
        self.assert_(solve(divisors=[3, -5], n=10) == 23)
        self.assert_(solve(divisors=[-3, -5], n=10) == 23)

    def test_n_zero(self):
        "zero n"

        self.assert_(solve(n=0) == 0)

    def test_n_neg(self):
        "negative n"

        self.assert_(solve(n=-10) == 0)

    def test_solve(self):
        "solution"

        self.assert_(solve() == 233168)

def run_tests(verbosity=0, tests=[]):
    tests = [ unittest.TestLoader().loadTestsFromTestCase(v)
            for k,v in globals().items()
            if k.startswith("Test") and (tests == [] or k in tests)]
    unittest.TextTestRunner(verbosity=verbosity).run(unittest.TestSuite(tests))

if __name__ == '__main__':

    run_tests()
