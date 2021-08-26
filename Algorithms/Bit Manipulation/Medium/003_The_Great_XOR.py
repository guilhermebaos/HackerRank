# hackerrank.com/challenges/the-great-xor/problem


def theGreatXor(x):
    x_bin = list(bin(x)[2:])
    x_len = len(x_bin)

    total = 0
    for index, bit in enumerate(x_bin):
        if bit == '0':
            position = x_len - index - 1

            # If q has a one in this position, the result will automatically be bigger than x, no mater the rest of q
            total += 2 ** position

    return total
