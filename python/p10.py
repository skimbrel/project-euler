from math import ceil
from math import sqrt

def eratosthenes_sieve(end):
    candidates = {}
    for i in xrange(2, end+1):
        candidates[i] = True

    for num in xrange(2, int(ceil(sqrt(end)))):
        if candidates[num]:
            for multiple in xrange(num ** 2, end + num, num):
                candidates[multiple] = False

    return [num for num in candidates.keys() if candidates[num]]

print sum(eratosthenes_sieve(2000000))
