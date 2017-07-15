import random


def random_all(size, start=0, end=None):
    if end is None:
        end = size ** 2
    x = []
    for _ in xrange(size):
        x.append(random.randint(start, end))
    return x
