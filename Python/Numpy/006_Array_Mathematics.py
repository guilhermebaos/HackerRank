# https://www.hackerrank.com/challenges/np-array-mathematics/problem

import numpy as np

n, m = list(map(int, input().split(' ')))

lst1 = []
for _ in range(n):
    lst1 += [input().split(' ')]
arr1 = np.array(lst1, int)

lst2 = []
for _ in range(n):
    lst2 += [input().split(' ')]
arr2 = np.array(lst2, int)

arr1.shape = (n, m)
arr2.shape = (n, m)

print(str(arr1 + arr2))
print(str(arr1 - arr2))
print(str(arr1 * arr2))
print(str(arr1 // arr2))
print(str(arr1 % arr2))
print(str(arr1 ** arr2))

