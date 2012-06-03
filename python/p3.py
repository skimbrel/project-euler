from math import floor
from math import sqrt

NUMBER = 600851475143


def is_prime(num):
    for i in xrange(2, int(floor(sqrt(num))) + 1):
        if num % i == 0:
            return False

    return True

print max([i for i in xrange(2, int(sqrt(NUMBER))) if NUMBER % i == 0 and is_prime(i)])
