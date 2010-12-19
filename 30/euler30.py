import unittest
import pyximport
pyximport.install()

import help34

def solve():
    help34.set_powers(5)
    rv = help34.solve()
    return rv


class TestHelper(unittest.TestCase):

    def test_4(self):

        help34.set_powers(4)
        self.assert_(help34.test(1634))
        self.assert_(help34.test(8208))
        self.assert_(help34.test(9474))
        self.assert_(help34.solve() == 19316)

def run_tests(verbosity=0, tests=[]):
    tests = [ unittest.TestLoader().loadTestsFromTestCase(v)
            for k,v in globals().items()
            if k.startswith("Test") and (tests == [] or k in tests)]
    unittest.TextTestRunner(verbosity=verbosity).run(unittest.TestSuite(tests))

if __name__ == '__main__':

    #run_tests()
    print solve()
