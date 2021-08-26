# https://www.hackerrank.com/challenges/counter-game/problem


# By converting the number to binary, we know that:

# Subtracting the next lower power of 2 is removing the 1 which is more to the left
# Dividing a power of 2 by two is also removing the first 1!
def counterGame(n):
    if n == 1:
        return 'Richard'

    n_bin = list(bin(n)[2:])

    # The total number of ones
    ones = n_bin.count('1')

    n_bin.reverse()
    # Number of zeroes after the last 1 in the number
    last_one = n_bin.index('1')

    # Louise wins if the number of turns is odd
    turns = ones + last_one - 1
    return 'Louise' if turns % 2 == 1 else 'Richard'

