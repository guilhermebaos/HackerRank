# https://www.hackerrank.com/challenges/aorb/problem


'''
# Convert an integer to a reverse binary
def reverse_bin(n):
    return list(map(int, list(f'{bin(n)[2:][::-1]}')))


# Bitwise or between two integers
def bitwise_or(a, b):
    # Make sure b > a
    c = a
    if a > b:
        a = b
        b = c

    # Convert both numbers into reverse binaries
    a = reverse_bin(int(a))
    b = reverse_bin(int(b))

    # Store the result
    bits = 200000
    result = [0 for _ in range(bits)]

    # Do the OR operation bit by bit
    index = 0
    for bit_a, bit_b in zip(a, b):
        result[index] = 1 if bit_a or bit_b else 0
        index += 1

    for bit_b in b[index:]:
        result[index] = bit_b
        index += 1

    # Convert the result to a list of strings, then to a string of the binary number, then to integer
    result.reverse()
    result = list(map(str, result))
    result = '0b' + ''.join(result)
    return int(result, 2)
'''


# Convert an integer to a normal binary (200_000 bits)
def normal_bin(n):
    return list(map(int, list(f'{bin(n)[2:]:0>{200_000}}')))


# Determine the obligatory bit switches that must be performed
def compare_with_result(k, a, b, c):
    index = 0
    for bit_a, bit_b, bit_c in zip(a[:], b[:], c[:]):
        # If the result is 0, both input bits must be zero
        if bit_c == 0:
            if bit_a == 1:
                k -= 1
                a[index] = 0
            if bit_b == 1:
                k -= 1
                b[index] = 0

        # If the result is 1, only one of the inputs has to be 1.
        else:

            # B is made to be 1 because A has to be as small as possible
            if bit_a == 0 and bit_b == 0:
                k -= 1
                b[index] = 1
        index += 1

        if k < 0:
            break

    return k, a, b, c


# Use the remaining changes to lower A
def lower_numbers(k, a, b):
    index = 0

    for bit_a, bit_b in zip(a[:], b[:]):

        # If both are 1, we can change the A bit to be 0 without affecting the OR
        if bit_a == 1 and bit_b == 1:
            a[index] = 0
            k -= 1

        # If A is 1 and B is 0, we can perform 2 changes to make A lower and keep the OR the same
        if bit_a == 1 and bit_b == 0 and k >= 2:
            a[index] = 0
            b[index] = 1
            k -= 2

        if k == 0:
            break

        index += 1

    return k, a, b


def aOrB(k, a, b, c):
    # Convert to decimal
    a = int(a, 16)
    b = int(b, 16)
    c = int(c, 16)

    # Convert to a binary list with 200k bits (each bit is an int)
    bin_a = normal_bin(a)
    bin_b = normal_bin(b)
    bin_c = normal_bin(c)

    # Check if we have enough moves to make the OR possible
    k, bin_a, bin_b, bin_c = compare_with_result(k, bin_a, bin_b, bin_c)
    if k < 0:
        return -1

    # Lower A as much as possible
    k, bin_a, bin_b = lower_numbers(k, bin_a, bin_b)

    # Convert to a binary string
    a = int('0b' + ''.join(list(map(str, bin_a))), 2)
    b = int('0b' + ''.join(list(map(str, bin_b))), 2)

    # Convert to a hexadecimal and return the values for A' and B'
    a = hex(a)[2:].upper()
    b = hex(b)[2:].upper()
    return a, b


print(aOrB(5, 'B9', '40', '5A'))
