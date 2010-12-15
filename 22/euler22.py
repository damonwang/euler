import csv 
from itertools import imap

__input__ = 'names.txt'

def name_to_alpha_val(name, 
        lookup=dict((c, ord(c) - ord('A') + 1) for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')):
    return sum(map(lookup.__getitem__, name))

def solve():

    with open(__input__) as inf:
        names = sorted(sum(csv.reader(inf), []))

    return sum(imap(lambda (i, name): (i+1) * name_to_alpha_val(name),
        enumerate(names)))

if __name__ == '__main__':

    print solve()



