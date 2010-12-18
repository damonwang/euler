import unittest

def factorial(n, cache=[1, 1, 2, 6, 24, 120,720, 5040, 40320, 362880]):
    try: return cache[n]
    except IndexError: 
        pass
    tmp = cache[-1]
    for i in range(len(cache) - 1, n):
        tmp *= i + 1
        cache.append(tmp)
    return tmp

def digits(n):
    '''
    digits(int n) -> [int]
    '''

    return map(int, str(n))

def solve(limit=10000000):
    '''
    Let f(n) = sum([ factorial(int(d)) for d in str(n) ])

    f(n) < factorial(9) * log10(n) < 10**6 * log10(n)

    So for all n > 10**7, f(n) < n and we can stop checking.
    '''

    return sum([ i for i in range(3, limit) 
        if i == sum([ factorial(int(d)) for d in str(i) ])])

class TestFactorial(unittest.TestCase):

    def test_cache(self):
        "serve from cache"

        self.assert_(factorial(1) == 1)
        self.assert_(factorial(2) == 2)
        self.assert_(factorial(5) == 120)

    def test_one(self):
        "one more than last cached"

        self.assert_(factorial(2, cache=[1, 1]) == 2)
        self.assert_(factorial(10) == 3628800)

    def test_many(self):
        "many more than last cached"

        self.assert_(factorial(10, cache=[1, 1]) == 3628800)

def run_tests(verbosity=0, tests=[]):
    tests = [ unittest.TestLoader().loadTestsFromTestCase(v)
            for k,v in globals().items()
            if k.startswith("Test") and (tests == [] or k in tests)]
    unittest.TextTestRunner(verbosity=verbosity).run(unittest.TestSuite(tests))

if __name__ == '__main__':

    run_tests()
