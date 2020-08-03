def icecreamParlor(m, arr):
    for pos1 in range(len(arr)):
        cost1 = arr[pos1]
        for pos2, cost2 in enumerate(arr[pos1 + 1:]):
            if cost1 + cost2 == m:
                return pos1 + 1, pos2 + 1 + pos1 + 1


print(icecreamParlor(4, [1, 4, 5, 3, 2]))