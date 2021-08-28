# https://www.hackerrank.com/challenges/xor-se/problem


"""
Slow Method:

# Each item of A can be writen as 0 XOR 1 XOR 2 XOR ... XOR i, where i is the index of the item
# Therefore, when we apply XOR to an entire sub-array, we are really only XORing the odds or the evens above A[l]
# That's because x XOR x an even number of times is 0!

# Items of A:
# 0
# 0 XOR 1
# 0 XOR 1 XOR 2                 -> Example l
# 0 XOR 1 XOR 2 XOR 3
# 0 XOR 1 XOR 2 XOR 3 XOR 4     -> Example r
# ...

# Doing XOR on all the numbers between l and r is equal to doing l XOR 4, because there are an even number of 3s


# Convert an integer to a reverse binary
def reverse_bin(n):
    return list(map(int, list(f'{bin(n)[2:][::-1]}')))


# XOR binary operation with an array of reversed binary numbers
def xor_reverse_bins(array):
    bits = 60
    result = [0 for _ in range(bits)]

    for num in array:
        for index, bit in enumerate(num):
            result[index] += bit

    for index, bit in enumerate(result):
        result[index] %= 2

    result.reverse()
    return list(map(str, result))


def xorSequence(l, r):
    # The parity of the numbers above l we'll XOR
    parity_above_l = ((r - l) % 2 + l % 2) % 2

    # All the numbers to XOR
    to_xor = []

    # Execute XOR on the numbers that have the parity found above
    for index in range(l + 1, r + 1):
        if index % 2 == parity_above_l:
            to_xor += [reverse_bin(index)]

    # Execute XOR on the numbers at A[l] if they don't cancel out
    if (r - l) % 2 == 0:
        for index in range(1, l + 1):
            to_xor += [reverse_bin(index)]

    total = xor_reverse_bins(to_xor)

    total = '0b' + ''.join(total)
    return int(total, 2)
"""


# Fast Method:

# The array A has the following pattern:
# A = [index, 1, index + 1, 0, index, 1, index + 1, 0, index, 1, ...] -> index, 1, index + 1, 0

# Knowing that (4n) XOR (4n + 3) = 3, we can massively simplify the problem


# Convert an integer to a reverse binary
def reverse_bin(n):
    return list(map(int, list(f'{bin(n)[2:][::-1]}')))


# XOR binary operation with an array of numbers
def xor_array(array):
    # Convert all numbers into reverse binaries
    for index, num in enumerate(array):
        array[index] = reverse_bin(int(num))

    # Store the result
    bits = 64
    result = [0 for _ in range(bits)]

    # Add the 1s
    for num in array:
        for index, bit in enumerate(num):
            result[index] += bit

    # Execute XOR on all the 1s
    for index, bit in enumerate(result):
        result[index] %= 2

    # Convert the result to a list of strings, then to a string of the binary number, then to integer
    result.reverse()
    result = list(map(str, result))
    result = '0b' + ''.join(result)
    return int(result, 2)


def xorSequence(l, r):
    # Execute XOR on the numbers that don't cancel out
    to_xor = []

    # Get the multiples of 4 above and below l and rx

    multiple_above_l = l - l % 4 + 4 if l % 4 != 0 else l
    multiple_below_r = r - r % 4

    # Get the number of entire index, 1, index + 1, 0 sequences there are
    entire_sequences = (multiple_below_r - multiple_above_l) // 4

    # Get the number of 1s, the number of 3s (4n XOR (4n + 3) = 3) and the indexes or indexes + 1 we have to XOR
    number_of_ones = entire_sequences
    number_of_threes = entire_sequences

    # Depending on where the cutoff point is for the incomplete sequence, we should also XOR different things
    if l % 4 == 1:
        number_of_ones += 1
        to_xor += [l + 2]
    elif l % 4 == 2:
        to_xor += [l + 1]

    if r % 4 == 0:
        to_xor += [r]
    elif r % 4 == 1:
        number_of_ones += 1
        to_xor += [r - 1]
    else:
        number_of_ones += 1
        number_of_threes += 1

    # If there is an odd number of 1s and/or 3s to XOR, do it, otherwise the result is 0
    if number_of_ones % 2 == 1:
        to_xor += [1]

    if number_of_threes % 2 == 1:
        to_xor += [3]

    return xor_array(to_xor)
