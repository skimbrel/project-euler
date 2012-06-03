def is_palindrome(num):
    stringified = str(num)
    backwards = reversed(stringified)
    for idx, char in enumerate(backwards):
        if stringified[idx] != char:
            return False
    return True

max_seen = 0
for i in xrange(100, 1000):
    for j in xrange(100, i):
        if is_palindrome(i * j) and i * j > max_seen:
            max_seen = i * j

print max_seen
