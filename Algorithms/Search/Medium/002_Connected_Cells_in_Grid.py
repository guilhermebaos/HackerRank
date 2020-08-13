def connectedCell(matrix):
    region_list = []
    len_row = len(matrix[0])
    len_col = len(matrix)
    for y, row in enumerate(matrix):
        for x, point in enumerate(row):
            if point == 1:
                region_size = 1
                to_watch = [(x, y)]
                matrix[y][x] = 2
                print('\n\n')
                while True:
                    temp = []
                    for start in to_watch:
                        s_x = start[0]
                        s_y = start[1]
                        if 0 <= s_x + 1 < len_row:
                            if matrix[s_y][s_x + 1] == 1:
                                region_size += 1
                                temp += [(s_x + 1, s_y)]
                                matrix[s_y][s_x + 1] = 2
                            if 0 <= s_y + 1 < len_col:
                                if matrix[s_y + 1][s_x + 1] == 1:
                                    region_size += 1
                                    temp += [(s_x + 1, s_y + 1)]
                                    matrix[s_y + 1][s_x + 1] = 2
                            if 0 <= s_y - 1 < len_col:
                                if matrix[s_y - 1][s_x + 1] == 1:
                                    region_size += 1
                                    temp += [(s_x + 1, s_y - 1)]
                                    matrix[s_y - 1][s_x + 1] = 2
                        if 0 <= s_x - 1 < len_row:
                            if matrix[s_y][s_x - 1] == 1:
                                region_size += 1
                                temp += [(s_x - 1, s_y)]
                                matrix[s_y][s_x - 1] = 2
                            if 0 <= s_y + 1 < len_col:
                                if matrix[s_y + 1][s_x - 1] == 1:
                                    region_size += 1
                                    temp += [(s_x - 1, s_y + 1)]
                                    matrix[s_y + 1][s_x - 1] = 2
                            if 0 <= s_y - 1 < len_col:
                                if matrix[s_y - 1][s_x - 1] == 1:
                                    region_size += 1
                                    temp += [(s_x - 1, s_y - 1)]
                                    matrix[s_y - 1][s_x - 1] = 2
                        if 0 <= s_x < len_row:
                            if 0 <= s_y + 1 < len_col:
                                if matrix[s_y + 1][s_x] == 1:
                                    region_size += 1
                                    temp += [(s_x, s_y + 1)]
                                    matrix[s_y + 1][s_x] = 2
                    to_watch = temp[:]
                    if len(to_watch) == 0:
                        break
                region_list += [region_size]
    return max(region_list)


print(connectedCell([[0, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 1, 0, 1, 0], [0, 1, 0, 1, 1], [0, 1, 1, 1, 0]]))
