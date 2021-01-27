def print_rangoli(size):
    width = 4 * size - 3
    max_ascii = size + 96
    for row in range(1, size + 1):
        row_list = []
        for char in range(row, 0, -1):
            ascii_code = max_ascii - char + 1
            row_list.insert(0, chr(ascii_code))
            if len(row_list) != 1:
                row_list.append(chr(ascii_code))
        print('-'.join(row_list).center(width, '-'))
    for row in range(size - 1, 0, -1):
        row_list = []
        for char in range(row, 0, -1):
            ascii_code = max_ascii - char + 1
            row_list.insert(0, chr(ascii_code))
            if len(row_list) != 1:
                row_list.append(chr(ascii_code))
        print('-'.join(row_list).center(width, '-'))
