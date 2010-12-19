import numpy as np
try:
    from scipy.constants import golden
except ImportError:
    golden = 1.6180339887498949
import unittest
import pyximport
pyximport.install()

from fibonacci import fibonacci

def solve(max_fib=int(4e6)):

    #Fibonacci sequence
    F = np.zeros(np.ceil(np.log(np.sqrt(5)*max_fib) / np.log(golden)),
            dtype='int64') 
    fibonacci(F)
    return F[F < int(4e6)][::3].sum()

class TestFibonacci(unittest.TestCase):

    def test_fib(self):
        "fibonacci sequence"

        expected = np.array([0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89,
            144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946,
            17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229,
            832040, 1346269, 2178309, 3524578, 5702887, 9227465,
            14930352, 24157817, 39088169], dtype='int64')
        F = np.zeros(expected.shape[0], dtype='int64')
        fibonacci(F)
        self.assert_((F == expected).all())

def run_tests(verbosity=0, tests=[]):
    tests = [ unittest.TestLoader().loadTestsFromTestCase(v)
            for k,v in globals().items()
            if k.startswith("Test") and (tests == [] or k in tests)]
    unittest.TextTestRunner(verbosity=verbosity).run(unittest.TestSuite(tests))

if __name__ == '__main__':

    #run_tests()
    print solve()
