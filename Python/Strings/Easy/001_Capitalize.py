def solve(s):
    list_s = []
    for letter in s:
        list_s += letter

    for pos, letter in enumerate(list_s):
        before = list_s[pos - 1]

        if before == ' ' or pos == 0:
            list_s[pos] = letter.upper()

    new_s = ''
    for letter in list_s:
        new_s += letter

    return new_s


test = 'hello world'
print(solve(test))
