# https://www.hackerrank.com/challenges/simplified-chess-engine/problem

# A 2D vector
class Vector2d:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y

        return Vector2d(x, y)


# POSSIBLE MOVES:
def horizontal():
    x = -3

    while x <= 3:
        yield x
        x += 1


# Representation of a Chess Piece
class Piece:
    # The piece has color and coordinates
    def __init__(self, color, coord):
        self.color = color
        self.coord = coord

    # Moving the piece
    def __add__(self, move):
        new_coord = self.coord + move

        if 1 > new_coord.x or new_coord.x > 4 or 1 > new_coord.y or new_coord.y > 4:
            raise ValueError('Piece out of the Board!')

        self.coord = new_coord


# The Rook can move anywhere from -3 to +3 in the x or y directions
class Rook(Piece):
    def __init__(self, color, coord):
        self.current_move = None
        self.move = self.get_move()
        super().__init__(color, coord)

    def get_move(self):
        while True:
            if not self.current_move:
                self.current_move = Vector2d(-3, 0)

            yield self.current_move

            if self.current_move.x == 3:
                raise StopIteration

            self.current_move.x += 1



a = Rook('White', Vector2d(1, 2))
a + Vector2d(1, -1)
a + Vector2d(1, 2)

print(a.coord.x, a.coord.y)
gen = a.move()
print(next(gen).x)
print(next(gen).x)
print(next(gen).x)
print(next(gen).x)
print(next(gen).x)
print(next(gen).x)
print(next(gen).x)
print(next(gen).x)