# https://www.hackerrank.com/challenges/lonely-integer/problem

def lonelyinteger(a):
    unique = []

    # If there are two instances of an item, it will be added and then removes, leaving only the unique item
    for item in a:
        if item in unique:
            unique.remove(item)
        else:
            unique += [item]

    return unique[0]
