# https://www.hackerrank.com/challenges/red-knights-shortest-path/problem

# Global Variables

# Constants
MOVE_NAMES = ['UL', 'UR', 'R', 'LR', 'LL', 'L']
PRIORITY_ORDER = [(-2, -1), (-2, 1), (0, 2), (2, 1), (2, -1), (0, -2)]


'''
Slow, but cool recursive generator

# Minimum length path found
min_path_len = 0


# Return the opposite move
def opposite_move(move):
    if move:
        return -move[0], -move[1]
    else:
        return 0, 0


# Recursive Generator for path finding
def path_finding(n, i_start, j_start, i_end, j_end, prev_move, path_len):
    global min_path_len

    # Delta coordinates
    delta_i = i_end - i_start
    delta_j = j_end - j_start

    # If the path is already larger than the minimum length path, return False
    if path_len >= min_path_len:
        return False

    # Start and End points
    end = (i_end, j_end)

    # Try every move in the order of Priority
    for move_index, move in enumerate(PRIORITY_ORDER):
        # If the move doesn't get us closer to target, skip it
        if ((move[0] >= 0 and delta_i >= 0) or (move[0] <= 0 and delta_i <= 0)) and\
                ((move[1] >= 0 and delta_j >= 0) or (move[1] <= 0 and delta_j <= 0)):

            # New position
            pos = (i_start + move[0], j_start + move[1])

            # If the position is invalid or if the new move is the opposite of the last more, we ignore it
            if pos[0] < 0 or pos[0] > n or pos[1] < 0 or pos[1] > n or move == opposite_move(prev_move):
                continue

            # If the new position is the goal, return the last piece of the path
            if pos == end:
                return [MOVE_NAMES[move_index]]

            # Otherwise, try every possible next step
            else:
                next_step_gen = path_finding(n, pos[0], pos[1], end[0], end[1], move, path_len + 1)
                while True:
                    try:
                        next_step = next(next_step_gen)

                        # If there is a possible next step, add it to the current path
                        if next_step:
                            yield [MOVE_NAMES[move_index]] + next_step
                        else:
                            yield False

                    # If the generator stops and returns a value, then a path is complete!
                    except StopIteration as error:
                        if error.value:
                            yield [MOVE_NAMES[move_index]] + error.value
                        break
'''


# Rules for finding every path
def path_finding(n, y_start, x_start, y_end, x_end):
    delta_y = y_end - y_start
    delta_x = x_end - x_start

    # Get the sign of the deltas
    if delta_y <= 0:
        delta_y_is_negative = True
    else:
        delta_y_is_negative = False

    if delta_x <= 0:
        delta_x_is_negative = True
    else:
        delta_x_is_negative = False

    # Get the absolute value of the deltas
    delta_y = abs(delta_y)
    delta_x = abs(delta_x)

    # Apply the rules
    path = []
    if delta_x_is_negative:
        if delta_y_is_negative:
            if delta_y / 2 < delta_x:
                path += ['UL'] * (delta_y // 2)
                path += ['L'] * ((delta_x - delta_y // 2) // 2)
            else:
                delta_y -= 2 * delta_x
                path += ['UL'] * delta_x
                path += ['UL'] * (delta_y // 4)
                path += ['UR'] * (delta_y // 4)
        elif delta_y == 0:
            path += ['L'] * (delta_x // 2)
        else:
            if delta_y / 2 < delta_x:
                path += ['LL'] * (delta_y // 2)
                path += ['L'] * ((delta_x - delta_y // 2) // 2)
            else:
                delta_y -= 2 * delta_x
                path += ['LR'] * (delta_y // 4)
                path += ['LL'] * delta_x
                path += ['LL'] * (delta_y // 4)
    elif delta_x == 0:
        pass
    else:
        if delta_y_is_negative:
            if delta_y / 2 < delta_x:
                path += ['UR'] * (delta_y // 2)
                path += ['R'] * ((delta_x - delta_y // 2) // 2)
            else:
                delta_y -= 2 * delta_x
                path += ['UL'] * (delta_y // 4)
                path += ['UR'] * (delta_y // 4)
                path += ['UR'] * delta_x
        elif delta_y == 0:
            path += ['R'] * (delta_x // 2)
        else:
            if delta_y / 2 < delta_x:
                path += ['R'] * ((delta_x - delta_y // 2) // 2)
                path += ['LR'] * (delta_y // 2)
            else:
                delta_y -= 2 * delta_x
                path += ['LR'] * (delta_y // 4)
                path += ['LR'] * delta_x
                path += ['LL'] * (delta_y // 4)
    return path


# Print the shortest path
def printShortestPath(n, i_start, j_start, i_end, j_end):
    min_path_len = n**2

    # See if it is possible to achieve the goal
    delta_i = i_end - i_start
    delta_j = j_end - j_start

    if delta_i % 2 == 1:
        print('Impossible')
        return
    elif delta_i % 4 == 0 and delta_j % 2 == 1:
        print('Impossible')
        return
    elif delta_i % 4 == 2 and delta_j % 2 == 0:
        print('Impossible')
        return

    # Try every path
    path = path_finding(n, i_start, j_start, i_end, j_end)
    print(len(path))
    print(' '.join(path))


printShortestPath(150, 24, 15, 46, 102)
