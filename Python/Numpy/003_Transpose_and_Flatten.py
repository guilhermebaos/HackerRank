# https://www.hackerrank.com/challenges/np-transpose-and-flatten/problem

import numpy as np

n, m = list(map(int, input().split(' ')))

arr = []
for _ in range(n):
    arr += [list(map(int, input().split(' ')))]

np_arr = np.array(arr, int)
print(np.transpose(arr))

np_arr = np_arr.flatten()
print(np_arr)
