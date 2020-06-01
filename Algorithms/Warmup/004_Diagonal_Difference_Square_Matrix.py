def diagonalDifference(arr):
    diagonal1 = 0
    diagonal2 = 0
    for pos, line in enumerate(arr):
        diagonal1 += line[pos]
        diagonal2 += line[len(arr)-1 - pos]
    return abs(diagonal1 - diagonal2)
