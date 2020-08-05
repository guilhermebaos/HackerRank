def minimumPath(move, size):
    a = [move[0], -move[0]]
    b = [move[1], -move[1]]
    mini_path = 0
    passed_pos = [(0, 0)]
    current_pos = [(0, 0)]
    while True:
        mini_path += 1
        possible_pos = []
        for pos in current_pos:
            for x_move in a:
                x = pos[0] + x_move
                if 0 <= x < size:
                    for y_move in b:
                        y = pos[1] + y_move
                        if 0 <= y < size:
                            if not passed_pos.__contains__((x, y)):
                                possible_pos += [(x, y)]
            for x_move in b:
                x = pos[0] + x_move
                if 0 <= x < size:
                    for y_move in a:
                        y = pos[1] + y_move
                        if 0 <= y < size:
                            if not passed_pos.__contains__((x, y)):
                                possible_pos += [(x, y)]
        possible_pos = list(set(possible_pos))
        current_pos = possible_pos[:]
        if possible_pos.__contains__((size - 1, size - 1)):
            return mini_path
        if len(possible_pos) == 0:
            return -1
        for pos in possible_pos:
            if not passed_pos.__contains__(pos):
                passed_pos += [pos]



def knightlOnAChessboard(n):
    pairs = []
    for a in range(1, n):
        pairs += [[]]
        for b in range(1, a + 1):
            pairs[-1] += [[a, b]]

    results = []
    for row in pairs:
        results += [[]]
        for pair in row:
            results[-1] += [minimumPath(pair, n)]

    org_results = []
    len_results = len(results)
    for pos, row in enumerate(results):
        org_results += [[]]
        for result in row:
            org_results[-1] += [result]
        for index in range(pos + 1, len_results):
            org_results[-1] += [results[index][pos]]

    return org_results


board = 5
solution = knightlOnAChessboard(board)

print('\n'.join([' '.join(map(str, x)) for x in solution]))
