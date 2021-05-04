# https://www.hackerrank.com/challenges/np-eye-and-identity/problem

import numpy as np
np.set_printoptions(legacy='1.13')

n, m = list(map(int, input().split(' ')))

myArr = np.array(np.eye(n, m, k=0))
print(myArr)
