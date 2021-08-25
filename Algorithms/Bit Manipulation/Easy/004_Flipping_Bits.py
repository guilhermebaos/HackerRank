# https://www.hackerrank.com/challenges/flipping-bits/problem

def flippingBits(n):
    # Convert n to a 32-bit integer
    n_bin = list(f'{bin(n)[2:]:0>32}')

    # Invert all the 0s and 1s in n
    n_bin_inv = [str(1 - int(digit)) for digit in n_bin]

    # Return the corresponding base 10 integer
    return int('0b' + ''.join(n_bin_inv), 2)
