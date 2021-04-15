# https://www.hackerrank.com/challenges/np-arrays/problem

import numpy


def arrays(arr):
    arr.reverse()
    arr = list(map(float, arr))
    return numpy.array(arr)
