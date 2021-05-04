# https://www.hackerrank.com/challenges/np-sum-and-prod/problem

import numpy as np

n, m = list(map(int, input().split(' ')))

myList = []
for _ in range(n):
    myList += [input().split(' ')]
myArr = np.array(myList, int)

print(np.prod(np.sum(myArr, axis=0)))
