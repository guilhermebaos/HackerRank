# https://www.hackerrank.com/challenges/floor-ceil-and-rint/problem

import numpy as np
np.set_printoptions(legacy='1.13')

myArr = input().split(' ')
myArr = np.array(myArr, float)

print(np.floor(myArr))
print(np.ceil(myArr))
print(np.rint(myArr))
