# https://www.hackerrank.com/challenges/np-concatenate/problem

import numpy as np

n, m, p = list(map(int, input().split(' ')))


lst1 = []
for _ in range(n):
    lst1 += [input().split(' ')]
arr1 = np.array(lst1, int)

lst2 = []
for _ in range(m):
    lst2 += [input().split(' ')]
arr2 = np.array(lst2, int)

print(np.concatenate((arr1, arr2)))

