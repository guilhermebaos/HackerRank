# https://www.hackerrank.com/challenges/np-array-mathematics/problem

import numpy as np

n, m = list(map(int, input().split(' ')))

arr1 = np.array(input().split(' '), int)
arr2 = np.array(input().split(' '), int)

arr1.shape = (n, m)
arr2.shape = (n, m)

print(str(arr1 + arr2))
print(str(arr1 - arr2))
print(str(arr1 * arr2))
print(str(arr1 // arr2))
print(str(arr1 % arr2))
print(str(arr1 ** arr2))
