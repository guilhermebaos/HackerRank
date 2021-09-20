# https://www.hackerrank.com/challenges/sansa-and-xor/problem

# XOR binary operation
def xor(a, b):
    a_bin = bin(a)[2:]
    b_bin = bin(b)[2:]

    max_len = max(len(a_bin), len(b_bin))

    a_bin = list(f'{a_bin:0>{max_len}}')
    b_bin = list(f'{b_bin:0>{max_len}}')

    result = '0b'

    for a_digit, b_digit in zip(a_bin, b_bin):
        result += '0' if a_digit == b_digit else '1'

    return int(result, 2)


# We use the fact that XOR is commutative and that:
# y XOR y XOR y etc. is 0 if we do it an even number of times and y if done an odd number of times
def sansaXor(arr):
    arr_len = len(arr)

    # The number of times each number appears in the XOR calculation depends only in it's position in the sub array
    appearances = [(index + 1) * (arr_len - index) for index in range(arr_len)]

    # Note: only later I learned that there are bitwise operators in python, such as ^ for XOR
    # Still, I'll keep this solution for future reference, as I will for all other Bit Manipulation Problems

    # Execute XOR when n appears an odd number of times in the final calculation
    result = 0
    for n, app in zip(arr[:], appearances):
        if app % 2 == 1:
            result = xor(result, n)

    return result
