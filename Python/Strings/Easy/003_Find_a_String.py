def count_substring(string, sub_string):
    matches = 0
    len_sub_string = len(sub_string)
    for start in range(len(string) - len_sub_string + 1):
        if string[start: start + len_sub_string] == sub_string:
            matches += 1
    return matches