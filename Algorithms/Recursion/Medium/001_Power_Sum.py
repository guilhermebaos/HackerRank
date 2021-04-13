# https://www.hackerrank.com/challenges/the-power-sum/problem

import math


# Create all possible powers that we can use for the sum
def powerSum(X, N):
    # Maximum exponential
    v_max = math.floor(pow(X, pow(N, -1))) + 1

    # All values until the max
    values_arr = list(map(pow, range(v_max), [N for _ in range(v_max)]))[1:]
    return recursive_sum(X, values_arr)


def recursive_sum(X, values):
    # Possible combinations
    ways_num = 0

    # Test if any number is a solution
    for index, v in enumerate(values):

        # If it is, add it to the count
        if v == X:
            ways_num += 1
            break

        # If it's over the solution, break the loop
        if v > X:
            break

        # If it isn't a solution, check if it part of one
        ways_num += recursive_sum(X - v, values[index + 1:])
    return ways_num


print(powerSum(100, 2))
