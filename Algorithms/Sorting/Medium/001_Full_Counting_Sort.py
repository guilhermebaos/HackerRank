def countSort(arr):
    for pair in arr[0:int(len(arr)/2)]:
        pair[1] = '-'

    related = {}
    numbers = []
    for pair in arr:
        pair[0] = int(pair[0])
        numbers += [pair[0]]
        try:
            related[pair[0]] += [pair[1]]
        except KeyError:
            related[pair[0]] = [pair[1]]

    maxi = 100
    string = []
    for pos in range(maxi):
        try:
            string += [related[pos]]
        except KeyError:
            pass

    for group in string:
        for letter in group:
            print(letter, end=' ')


test = [['0', 'a'], ['1', 'b'], ['0', 'c'], ['1', 'd']]

countSort(test)
