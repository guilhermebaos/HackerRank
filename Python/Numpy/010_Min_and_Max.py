# https://www.hackerrank.com/challenges/np-min-and-max/problem

import numpy as np

n, m = list(map(int, input().split(' ')))

myList = []
for _ in range(n):
    myList += [input().split(' ')]
myArr = np.array(myList, int)

print(np.max(np.min(myArr, axis=1)))
