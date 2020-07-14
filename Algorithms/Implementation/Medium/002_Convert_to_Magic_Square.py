# A soma tem de ser de 15, pois 1+2+3+4+5+6+7+8+9 = 45 e 45/3 = 15 (A soma de três linhas/colunas tem de ser a soma de todos os números)
# O 5 tem de estar no meio, se não não há pares suficientes para perfazer 15
# Os pares só podem trocar de lugar um com o outro
# Se um par trocar, todos os outros teriam que trocar

# Logo,
# Só há um magic square

def formingMagicSquare(s):
    magic_squares = [[[8, 3, 4],
                      [1, 5, 9],
                      [6, 7, 2]],
                     [[4, 9, 2],
                      [3, 5, 7],
                      [8, 1, 6]],
                     [[2, 7, 6],
                      [9, 5, 1],
                      [4, 3, 8]],
                     [[6, 1, 8],
                      [7, 5, 3],
                      [2, 9, 4]],
                     [[8, 1, 6],
                      [3, 5, 7],
                      [4, 9, 2]],
                     [[2, 9, 4],
                      [7, 5, 3],
                      [6, 1, 8]],
                     [[4, 3, 8],
                      [9, 5, 1],
                      [2, 7, 6]],
                     [[6, 7, 2],
                      [1, 5, 9],
                      [8, 3, 4]]]

    costs = []
    for square in magic_squares:
        costs += [delta(s, square)]
    return min(costs)


def delta(list_from, list_to):
    cost = 0
    for row_from, row_to in zip(list_from, list_to):
        for num_from, num_to in zip(row_from, row_to):
            cost += abs(num_from - num_to)
    return cost


test = [[4, 5, 8],
        [2, 4, 1],
        [1, 9, 7]]

print(formingMagicSquare(test))
