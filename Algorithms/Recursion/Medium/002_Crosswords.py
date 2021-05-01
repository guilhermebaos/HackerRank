# https://www.hackerrank.com/challenges/crossword-puzzle/problem
# I Should have used numpy

import re


# Defines the characteristics of an empty space: The constant coordinate, start and end
class EmptySpace(object):
    def __init__(self, start, end, const):
        self.start = start
        self.end = end
        self.const = const


# Returns a simple dictionary, to work with the 2 dimensions of the crosswords
def dict_2d():
    return {
        'rows': [],
        'columns': []
    }


# Finds all the empty spaces in a string
def find_spaces(string):
    return re.finditer(r'-+', string)


# Check if all items in array are something
def check_if_full(arr):
    for i in arr:
        if not i:
            return False
    return True


# Recursively finds the order in which the words fit into the empty spaces, rows first, then columns
def fit_words(words, possibilities, intersections, current_map=False, index=0):
    # Initialize the 'map', which represents the solution array
    if not current_map:
        current_map = []
        for _ in possibilities:
            current_map += [False]

    # If the map is full, return it
    if check_if_full(current_map):
        return current_map

    # Fits one word into the next space
    space = current_map[index]
    inter = intersections[index]

    # If there are no intersections, it's as if it always has the right letter in the intersection
    if len(inter) == 0:
        letter1 = True
        letter2 = True

    # If the space isn't yet filled, put a word in it that fits the intersections (it already has the right size)
    if not space:
        for p in possibilities[index]:
            if p in words:
                words.remove(p)
                current_map[index] = p

                # Check the letters at the intersection, if at least one of them isn't filled, then the word will fit
                for i in inter:
                    try:
                        letter1 = current_map[i[0][0]][i[0][1]]
                        letter2 = current_map[i[1][0]][i[1][1]]
                    except TypeError:
                        letter1 = True
                        letter2 = True

                # If it doesn't fit the intersection, remove the word
                if letter1 != letter2:
                    words += [p]
                    current_map[index] = False

                # If it fits, try to put a word in the rest of the spaces
                else:
                    recursive_map = fit_words(words, possibilities, intersections, current_map, index + 1)
                    if not recursive_map:
                        words += [p]
                        current_map[index] = False
                    else:
                        return recursive_map
    return False


# Put a word inside a string (column or row of the crosswords), using lists
def word_into_string(str_arr, start, end, word):
    str_arr = list(str_arr)
    word = list(word)
    str_arr[start:end + 1] = word
    return ''.join(str_arr)


# Put the words into the crossword
def fit_words_on_crossword(crossword, empty_spaces, solutions):
    # Fill the empty row spaces with the right words
    solution_index = 0
    for space_row in empty_spaces['rows']:
        crossword[space_row.const] = word_into_string(crossword[space_row.const], space_row.start, space_row.end, solutions[solution_index])
        solution_index += 1

    # Rotate array
    crossword_columns = ['' for _ in crossword]
    for row in crossword:
        for index, item in enumerate(row):
            crossword_columns[index] += item

    # Fill the empty column spaces with the right words
    for space_col in empty_spaces['columns']:
        crossword_columns[space_col.const] = word_into_string(crossword_columns[space_col.const], space_col.start, space_col.end, solutions[solution_index])
        solution_index += 1

    # Rotate array
    crossword_row = ['' for _ in crossword]
    for col in crossword_columns:
        for index, item in enumerate(col):
            crossword_row[index] += item

    # Return filled array in the correct orientation
    return crossword_row


# Main funtion
def crosswordPuzzle(crossword, words):
    # Split the words and get their length
    words = words.split(';')
    words_len = list(map(len, words))

    # Empty spaces, with the format (START, END, CONST_COORDINATE)
    empty_spaces = dict_2d()

    # Coordinates of the intersections, each index is the index of the row the intersection corresponds to
    intersections = []

    # Find the empty spaces in the rows
    crossword_columns = [[''] for _ in crossword]
    for y_pos, row in enumerate(crossword):
        matches = find_spaces(row)

        for m in matches:
            span = m.span()
            length = span[1] - span[0]
            if length > 1:
                empty_spaces['rows'] += [EmptySpace(span[0], span[1] - 1, y_pos)]
                intersections += [[]]

        # While doing that, create a rotated array
        for index, item in enumerate(row):
            crossword_columns[index][0] += item

    # Find the empty spaces in the columns and find the intersections
    column_index = len(empty_spaces['rows']) - 1
    for x_pos, column in enumerate(crossword_columns):
        column = ''.join(column)
        crossword_columns[x_pos] = column
        matches = find_spaces(column)

        for m in matches:
            span = m.span()
            length = span[1] - span[0]
            if length > 1:
                column_index += 1
                new_column = EmptySpace(span[0], span[1] - 1, x_pos)
                empty_spaces['columns'] += [new_column]
                intersections += [[]]

                # Get the intersections between row and column words
                for row_index, e_s_row in enumerate(empty_spaces['rows']):
                    if new_column.start <= e_s_row.const <= new_column.end and e_s_row.start <= new_column.const <= e_s_row.end:
                        row_pos = new_column.const - e_s_row.start
                        column_pos = e_s_row.const - new_column.start
                        intersections[row_index] += [[[row_index, row_pos], [column_index, column_pos]]]
                        intersections[column_index] += [[[row_index, row_pos], [column_index, column_pos]]]

    # Possible words that can go into each space, based on length
    possibilities = []
    for key in empty_spaces:
        for e_s in empty_spaces[key]:
            possibilities += [[]]
            length = e_s.end - e_s.start + 1
            for index, w_l in enumerate(words_len):
                if length == w_l:
                    possibilities[-1] += [words[index]]

    # Get the words that go into each empty space, in order
    solution_arr = fit_words(words, possibilities, intersections)

    # Return the array with the words in the right position
    return fit_words_on_crossword(crossword, empty_spaces, solution_arr)


result = crosswordPuzzle(
    ['+-++++++++', '+-++-+++++', '+-------++', '+-++-+++++', '+-++-+++++', '+-++-+++++', '++++-+++++', '++++-+++++',
     '++++++++++', '----------'], 'CALIFORNIA;NIGERIA;CANADA;TELAVIV')

print('\n'.join(result))
print('\n')
