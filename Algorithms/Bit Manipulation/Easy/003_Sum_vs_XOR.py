# https://www.hackerrank.com/challenges/sum-vs-xor/problem

'''
Slow Version:

# See if the XOR is equal to n
def isSumEqualToXor(x, n):
    x_bin = list(bin(x)[2:])
    n_bin = list(bin(n)[2:])
    sum_bin = list(bin(x + n)[2:])

    # If the lengths the sum and the xor are different, the corresponding numbers will also be
    # The length of the xor is the length of the biggest of the two numbers, which is n
    n_len = len(n_bin)
    if n_len != len(sum_bin):
        return False

    # By reversing the binaries, we only have to XOR up to the last digit in b
    x_bin.reverse()
    n_bin.reverse()
    sum_bin.reverse()

    # XOR a digit at a time. If the digits are different, we don't have to continue the binary operation
    for x_digit, n_digit, sum_digit in zip(x_bin, n_bin, sum_bin):
        next_digit = '0' if x_digit == n_digit else '1'
        if sum_digit != next_digit:
            return False

    # The sum of two numbers can affect the next digit after the end of the smallest one
    x_len = len(x_bin)
    if x_len < n_len:
        if sum_bin[x_len] != n_bin[x_len]:
            return False

    return True


# Brute force all value of x that are smaller than n
def sumXor(n):
    n = int(n)

    total = 0
    for x in range(n + 1):
        if isSumEqualToXor(x, n):
            total += 1

    return total
'''


# Fast Version
# An XOR is equal to a SUM when the numbers' don't have 1s in the same position
def sumXor(n):
    if n == 0:
        return 1

    n = int(n)

    # x can be any permutation of 0s and 1s, as long as it is all 0s in the places where n has a 1
    n_bin = list(bin(n)[2:])
    n_zeroes = n_bin.count('0')

    return 2 ** n_zeroes
