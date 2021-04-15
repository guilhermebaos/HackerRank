# https://www.hackerrank.com/challenges/np-shape-reshape/problem?h_r=next-challenge&h_v=zen

import numpy as np

arr = input().split(' ')
np_arr = np.array(arr, int)
np_arr.shape = (3, 3)

print(np_arr)
