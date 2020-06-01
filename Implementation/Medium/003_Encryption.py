import math


def encryption(s=''):
    string = s.replace(' ', '')
    lenght = len(string)

    rows = math.floor(lenght**0.5)
    colums = math.ceil(lenght**0.5)         # Essencialy the number os letters per row
    if rows * colums < lenght:
        rows = colums

    grid = []
    for c in range(0, rows):
        grid += [string[c*colums:(c+1)*colums]]

    to_print = []
    for c in range(0, colums):
        to_print += [['']]

    for word in to_print:
        for row in grid:
            try:
                word[0] += row[to_print.index(word)]
            except IndexError:
                word += ['']

    encrypted = ''
    for word in to_print:
        encrypted += word[0] + ' '
    return encrypted.rstrip()
