"""
Tests is Pythagorean
"""

# Author: Julian Garcia, based on code by Brendon Taylor

from pythagorian import create_triple
from random import randint


def test_triple(triple):
    return triple[0] * triple[0] + triple[1] * triple[1] ==
    triple[2] * triple[2]


def test_pythagorean():
    MAX_VALUE = 1000
    MAX_TEST_CASES = 100

    # Test m,n = 0
    assert test_triple(create_triple(0, 0)), "Failed test for (0,0)"
    # Test random values
    for i in range(MAX_TEST_CASES):
        m = randint(-MAX_VALUE, MAX_VALUE)
        n = randint(-MAX_VALUE, MAX_VALUE)
        assert test_triple(create_triple(m, n)), "Failed test for ({},{})".format(m, n)

    # Test random positive values
    for i in range(MAX_TEST_CASES):
        m = randint(1, MAX_VALUE)
        n = randint(1, MAX_VALUE)
        assert test_triple(create_triple(m, n)), "Failed test for ({},{})".format(m, n)

if __name__ == '__main__':
    test_pythagorean()
