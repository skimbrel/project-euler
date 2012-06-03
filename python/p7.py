"""Find the 10001st prime."""
from math import floor
from math import sqrt

# Let's try the dumbest thing that might work.
def is_prime(num):
    if num in (0, 1):
        return False
    for i in xrange(2, int(floor(sqrt(num))) + 1):
        if num % i == 0:
            return False
    return True

def integers():
    n = 0
    while True:
        yield n
        n += 1

def find_nth_prime(n):
    primes_seen = 0
    last_prime = 0
    ints = integers()
    while primes_seen < n:
        candidate = ints.next()
        if is_prime(candidate):
            last_prime = candidate
            primes_seen += 1

    return last_prime

print find_nth_prime(10001)
