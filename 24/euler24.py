from itertools import islice, permutations 

def solve(elts=range(10), n=999999):
    '''
    solve(iterable elts=range(10), int n=999999) -> tuple

    returns the (zero-indexed) nth lexicographic permutation of the elts
    iterable.
    '''

    return next(islice(permutations(elts, len(elts)), n, n+1))
