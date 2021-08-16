# https://www.hackerrank.com/challenges/simplified-chess-engine/problem

# CONVERT X-COORDINATES TO NUMBERS
def letters_to_numbers(letter):
    if letter == 'A':
        return 1
    if letter == 'B':
        return 2
    if letter == 'C':
        return 3
    if letter == 'D':
        return 4


# POSSIBLE MOVES:
def horizontal():
    return [[-3, 0], [-2, 0], [-1, 0], [1, 0], [2, 0], [3, 0]]


def vertical():
    return [[0, -3], [0, -2], [0, -1], [0, 1], [0, 2], [0, 3]]


def diagonal():
    return [[-3, -3], [-2, -2], [-1, -1], [1, 1], [2, 2], [3, 3], [-3, 3], [-2, 2], [-1, 1], [1, -1], [2, -2], [3, -3]]


def horse():
    return [[1, 2], [-1, 2], [1, -2], [-1, -2], [2, 1], [2, -1], [-2, 1], [-2, -1]]


# REPRESENTATION OF A CHESS PIECE
class Piece:
    # The piece has color and coordinates
    def __init__(self, color, type_of_piece, coord):
        self.color = color
        self.piece = type_of_piece
        self.coord = coord

    # Moving the piece
    def __add__(self, move):
        new_coord = [self.coord[0] + move[0], self.coord[1] + move[1]]

        if new_coord[0] < 1 or new_coord[0] > 4 or new_coord[1] < 1 or new_coord[1] > 4:
            raise ValueError('Piece out of the Board!')

        return new_coord


# Check is a move type is possible
def check_move(current_piece, other_pieces, move_type):
    possible_moves = []

    # Is a piece wants to move horizontally, check the x values for pieces on the same row
    if move_type == 'horizontal':
        min_x, max_x = None, None
        for different_piece in other_pieces:

            # x-coordinates of the pieces to the left and right of this one
            if different_piece.coord[1] == current_piece.coord[1]:
                if different_piece.coord[0] < current_piece.coord[0]:
                    if (min_x and different_piece.coord[0] > min_x) or (not min_x):
                        min_x = different_piece.coord[0]

                else:
                    if (max_x and different_piece.coord[0] < max_x) or (not max_x):
                        max_x = different_piece.coord[0]

        # If a horizontal move doesn't jump over a piece, it's valid
        for move in horizontal():
            possible_moves += [move]

            # Working with the maximum values for new_coords
            try:
                new_coords = current_piece + move

                if min_x and min_x > new_coords[0]:
                    possible_moves.remove(move)
                if max_x and max_x < new_coords[0]:
                    possible_moves.remove(move)
            except ValueError:
                possible_moves.remove(move)

    # Check what vertical moves are possible
    elif move_type == 'vertical':
        min_y, max_y = None, None
        for different_piece in other_pieces:

            # y-coordinates of the pieces to the bottom and top of this one (they have to be on the same col -> same x)
            if different_piece.coord[0] == current_piece.coord[0]:
                if different_piece.coord[1] < current_piece.coord[1]:
                    if (min_y and different_piece.coord[1] > min_y) or (not min_y):
                        min_y = different_piece.coord[1]

                else:
                    if (max_y and different_piece.coord[1] < max_y) or (not max_y):
                        max_y = different_piece.coord[1]

        # If a vertical move doesn't jump over a piece, it's valid
        for move in vertical():
            possible_moves += [move]

            # Working with the maximum values for new_coords
            try:
                new_coords = current_piece + move

                if min_y and min_y > new_coords[1]:
                    possible_moves.remove(move)
                if max_y and max_y < new_coords[1]:
                    possible_moves.remove(move)
            except ValueError:
                possible_moves.remove(move)

    # Check what diagonal moves are possible
    elif move_type == 'diagonal':
        positive_x_min_y, positive_x_max_y = None, None
        negative_x_min_y, negative_x_max_y = None, None

        for different_piece in other_pieces:
            delta_coord = [different_piece.coord[0] - current_piece.coord[0],
                           different_piece.coord[1] - current_piece.coord[1]]

            # Check if different_piece is in the same diagonal as current_piece
            if abs(delta_coord[0]) != abs(delta_coord[1]):
                continue

            # If they are in the same diagonal, identify the quadrant which they are in
            if delta_coord[0] > 0:
                if delta_coord[1] < 0:
                    if (positive_x_min_y and delta_coord[1] > positive_x_min_y) or (not positive_x_min_y):
                        positive_x_min_y = delta_coord[1]

                else:
                    if (positive_x_max_y and delta_coord[1] < positive_x_max_y) or (not positive_x_max_y):
                        positive_x_max_y = delta_coord[1]

            else:
                if delta_coord[1] < 0:
                    if (negative_x_min_y and delta_coord[1] > negative_x_min_y) or (not negative_x_min_y):
                        negative_x_min_y = delta_coord[1]
                else:
                    if (negative_x_max_y and delta_coord[1] < negative_x_max_y) or (not negative_x_max_y):
                        negative_x_max_y = delta_coord[1]


        # If a diagonal move doesn't jump over a piece, it's valid
        for move in diagonal():
            possible_moves += [move]

            # Working with the maximum values for move
            try:
                new_coords = current_piece + move

                if move[0] > 0:
                    if positive_x_min_y and positive_x_min_y > move[1]:
                        possible_moves.remove(move)
                    elif positive_x_max_y and positive_x_max_y < move[1]:
                        possible_moves.remove(move)

                else:
                    if negative_x_min_y and negative_x_min_y > move[1]:
                        possible_moves.remove(move)
                    elif negative_x_max_y and negative_x_max_y < move[1]:
                        possible_moves.remove(move)

            except ValueError:
                possible_moves.remove(move)

    return possible_moves


# Creates a generator with all possible moves a piece can make, given a certain board
def move_generator(current_piece, same_color, other_color):
    possible_moves = []
    if current_piece.piece == 'R':
        possible_moves += check_move(current_piece, same_color + other_color, 'horizontal')
        possible_moves += check_move(current_piece, same_color + other_color, 'vertical')

    elif current_piece.piece == 'B':
        possible_moves += check_move(current_piece, same_color + other_color, 'diagonal')

    elif current_piece.piece == 'N':
        possible_moves += horse()

    elif current_piece.piece == 'Q':
        possible_moves += check_move(current_piece, same_color + other_color, 'horizontal')
        possible_moves += check_move(current_piece, same_color + other_color, 'vertical')
        possible_moves += check_move(current_piece, same_color + other_color, 'diagonal')

    for m in possible_moves:
        yield m


# Detect Collisions between pieces
def detect_collisions(new_coord, same_color, other_color):
    # If the pieces are the same color, raise an Exception
    for same in same_color:
        if same.coord == new_coord:
            raise ValueError

    # If they're different colors, return the piece, in order for it to be removed
    for other in other_color:
        if other.coord == new_coord:
            return other

    return None


# See if white can win in less than m moves
def can_white_win(moving_now, moving_next, moves, current_move=1):
    # If we're over the move limit, white can't win
    if current_move > moves:
        return False

    # See whose turn it is
    if current_move % 2 == 1:
        moving_color = 'White'
    else:
        moving_color = 'Black'

    # For every piece of the color that's moving now, try every move possible that it can make
    results = []
    for index_piece, current_piece in enumerate(moving_now):
        move_gen = move_generator(current_piece, moving_now[:index_piece] + moving_now[index_piece + 1:], moving_next)

        # Try every move of the selected piece
        while True:
            try:
                next_move = next(move_gen)
                new_coord = current_piece + next_move

                collision = detect_collisions(new_coord, moving_now[:index_piece] + moving_now[index_piece + 1:],
                                              moving_next)

                new_next = moving_next[:]
                if collision:
                    new_next.remove(collision)
                    if collision.piece == 'Q':
                        if moving_color == 'White':
                            return True
                        else:
                            return False

                new_now = moving_now[:]
                new_now[index_piece] = Piece(current_piece.color, current_piece.piece, new_coord)

                results += [can_white_win(new_next, new_now, moves, current_move + 1)]

                # If white has one way to win, return True
                if moving_color == 'White' and results[-1]:
                    return True

                # If black has one way to win against the previous white move, white loses
                if moving_color == 'Black' and not results[-1]:
                    return False

            except StopIteration:
                break
            except RuntimeError:
                pass
            except ValueError:
                pass

    # Check the results of the following moves

    # If white had no way to win, white loses
    if moving_color == 'White':
        return False

    # If black had no way to win, white wins
    else:
        return True


# Main Function
def simplifiedChessEngine(whites, blacks, moves):
    new_whites, new_blacks = [], []
    for w in whites:
        new_whites += [Piece('White', w[0], [letters_to_numbers(w[1]), int(w[2])])]

    for b in blacks:
        new_blacks += [Piece('Black', b[0], [letters_to_numbers(b[1]), int(b[2])])]

    result = can_white_win(new_whites, new_blacks, moves * 2 - 1)
    if result:
        return 'YES'
    else:
        return 'NO'


print('\n\n')
print(simplifiedChessEngine(
    [['Q', 'C', '1']],
    [['Q', 'B', '3']],
    4
))
print(simplifiedChessEngine(
    [['N', 'C', '2'], ['N', 'A', '1'], ['R', 'D', '4'], ['R', 'B', '4'], ['Q', 'B', '2']],
    [['R', 'A', '2'], ['Q', 'C', '1']],
    1
))
print('\n\n')
print(simplifiedChessEngine(
    [['N', 'C', '2'], ['R', 'A', '1'], ['Q', 'D', '4']],
    [['R', 'A', '4'], ['R', 'B', '4'], ['N', 'A', '3'], ['N', 'C', '3'], ['Q', 'A', '2']],
    6
))
