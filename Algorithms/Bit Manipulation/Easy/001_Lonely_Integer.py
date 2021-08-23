# https://www.hackerrank.com/challenges/lonely-integer/problem

def lonelyinteger(a):
    unique = []
    for item in a:
        if item in unique:
            unique.remove(item)
        else:
            unique += [item]

    return unique[0]
