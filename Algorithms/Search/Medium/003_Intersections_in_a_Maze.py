# https://www.hackerrank.com/challenges/count-luck/problem

# Count the number of intersections in the correct path of a maze
def countLuck(matrix, k):

    # Get the start and the end coordinates
    for y, row in enumerate(matrix):
        if row.__contains__('M'):
            start = (row.index('M'), y)
        if row.__contains__('*'):
            end = (row.index('*'), y)

    # Matrix coordinates
    max_x = len(matrix[0])
    max_y = len(matrix)

    # Global variables for solving the maze and identifying the correct path
    look_for = [start]
    been_to = []
    paths = [[start]]
    intersections = []

    # Loop to Solve the Maze
    done = False
    while len(look_for) != 0:

        # Declare variables
        new_look_for = []
        path_to_pop = []
        num_new_paths = 0

        # For every possible different path
        for path_index, begin in enumerate(look_for):

            path_index += num_new_paths     # Add a delta index to the current path index, because new paths were create
            looking_at = []                 # Reset the different paths we could follow

            # Look at every possible cell next to the one we have selected
            for delta in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                new_cell = (begin[0] + delta[0], begin[1] + delta[1])

                if -1 < new_cell[0] < max_x and -1 < new_cell[1] < max_y:
                    if new_cell not in been_to and matrix[new_cell[1]][new_cell[0]] == '.': # If the cell is new and is empty
                        looking_at += [new_cell]
                        new_look_for += [new_cell]
                        been_to += [new_cell]
                    elif new_cell == end:                                                   # If the cell is the end
                        looking_at += [new_cell]
                        new_look_for += [new_cell]
                        been_to += [new_cell]
                        done = True

            # Store the paths with the new cells
            len_looking_at = len(looking_at)
            if len_looking_at > 1:              # If the current path diverges
                intersections += [begin]            # Mark the cell as an intersection
                for delta_index, new_path in enumerate(looking_at[1:]):     # Create new paths
                    paths.insert(path_index + delta_index + 1, paths[path_index] + [new_path])
                num_new_paths += len_looking_at - 1
            if len_looking_at > 0:              # If there is only one option
                paths[path_index] += [looking_at[0]]
            else:                               # If it is a dead-end
                path_to_pop += [path_index]

        # Update what the paths and what is at the end of each path
        look_for = new_look_for[:]

        path_to_pop.sort(reverse=True)
        for index in path_to_pop:
            paths.pop(index)

        if done:
            break

    # The correct path contains the end cell
    for p in paths:
        if end in p:
            correct_path = p

    # See how many cells from the correct path are intersections
    count = len(set(correct_path).intersection(set(intersections)))

    if count == k:
        return 'Impressed'
    else:
        return 'Oops!'


countLuck(['.X.X......X', '.X*.X.XXX.X', '.XX.X.XM...', '......XXXX.'], 3)
