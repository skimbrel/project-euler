"""Find the 3-tuple (a, b, c) such that a < b < c, a**2 + b**2 == c**2, and sum(a,b,c) = 1000."""

def find_tuple():
    for c in xrange(0, 1000):
        for b in xrange(0, c):
            for a in xrange(0, b):
                if a ** 2 + b ** 2 == c ** 2 and sum([a, b, c]) == 1000:
                    print a * b * c
                    return

find_tuple()
