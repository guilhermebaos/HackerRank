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
    x = -3

    while x <= 3:
        yield [x, 0]
        x += 1

        if x == 0:
            x += 1


def vertical():
    y = -3

    while y <= 3:
        yield [0, y]
        y += 1

        if y == 0:
            y += 1


def diagonal():
    x = -3
    y = -3

    while x <= 3:
        yield [x, y]
        yield [x, y * -1]
        x += 1
        y += 1

        if x == 0:
            x += 1
            y += 1


def horse():
    move = [1, 2]

    for inverted in [False, True]:
        if inverted:
            move = [move[1], move[0]]
        for x in [-1, 1]:
            for y in [-1, 1]:
                yield [move[0] * x, move[1] * y]


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

    # All the possible moves it could make in a 4 x 4 board
    def move_generator(self):
        if self.piece == 'R':
            h = horizontal()
            while True:
                yield next(h)

        elif self.piece == 'B':
            d = diagonal()
            while True:
                yield next(d)

        elif self.piece == 'N':
            h = horse()
            while True:
                yield next(h)

        elif self.piece == 'Q':
            h = horizontal()
            while True:
                try:
                    yield next(h)
                except StopIteration:
                    break

            v = vertical()
            while True:
                try:
                    yield next(v)
                except StopIteration:
                    break

            d = diagonal()
            while True:
                yield next(d)


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
    if current_move > moves:
        return False

    if current_move % 2 == 1:
        moving_color = 'White'
    else:
        moving_color = 'Black'

    # For every piece of the color that's moving now, try every move possible
    results = []
    for index_piece, current_piece in enumerate(moving_now):
        move_gen = current_piece.move_generator()

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

            except StopIteration:
                break
            except RuntimeError:
                pass
            except ValueError:
                pass

    # Check the results of the following moves

    # For white to win, it has to win against every black move
    if moving_color == 'White':
        for r in results:
            if not r:
                return False
        return True

    # For black to lose, there has to be one way for white to win after this specific move
    else:
        for r in results:
            if r:
                return True
        return False


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


print(simplifiedChessEngine(
    [['N', 'C', '2'], ['N', 'A', '1'], ['R', 'D', '4'], ['R', 'B', '4'], ['Q', 'B', '2']],
    [['R', 'A', '2'], ['Q', 'C', '1']],
    1
))
print('\n\n')
print(simplifiedChessEngine(
    [['Q', 'C', '1']],
    [['Q', 'B', '3']],
    4
))
print('\n\n')
print(simplifiedChessEngine(
    [['N', 'C', '2'], ['R', 'A', '1'], ['Q', 'D', '4']],
    [['R', 'A', '4'], ['R', 'B', '4'], ['N', 'A', '3'], ['N', 'C', '3'], ['Q', 'A', '2']],
    6
))
