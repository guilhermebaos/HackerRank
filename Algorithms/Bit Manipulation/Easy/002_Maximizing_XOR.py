# https://www.hackerrank.com/challenges/maximizing-xor/problem

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


def maximizingXor(l, r):
    results = []
    for a in range(l, r + 1):
        for b in range(a, r + 1):
            results += [xor(a, b)]

    return max(results)
