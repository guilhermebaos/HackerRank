# https://www.hackerrank.com/challenges/np-zeros-and-ones/problem

import numpy as np

dimensions = tuple(map(int, input().split(' ')))

print(np.zeros(dimensions, dtype=int))
print(np.ones(dimensions, dtype=int))
