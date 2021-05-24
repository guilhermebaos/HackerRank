# https://www.hackerrank.com/challenges/np-mean-var-and-std/problem

# Variance: Mean of all the squared deviations from mean of the set of numbers
# Standard Deviation: Square root of variance

import numpy as np

n, m = list(map(int, input().split(' ')))

myList = []
for _ in range(n):
    myList += [input().split(' ')]
myArr = np.array(myList, int)
myArr.shape = (n, m)

print(np.mean(myArr, axis=1))
print(np.var(myArr, axis=0))
print(round(float(np.std(myArr)), 11))  # Rounded for compatibility in the challenge
