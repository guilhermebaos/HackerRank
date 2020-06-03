def superReducedString(s=''):
    if len(s) == 0:
        return 'Empty String'

    s_list = []
    for letter in s:
        s_list += [letter]

    to_break = False
    while True:
        pos = 0
        while True:
            pos += 1
            if pos >= len(s_list):
                to_break = True
                break
            if s_list[pos] == s_list[pos-1]:
                s_list.pop(pos)
                s_list.pop(pos - 1)
                break
            elif pos >= len(s_list):
                to_break = True
                break
        if to_break:
            break

    if len(s_list) == 0:
        return 'Empty String'
    else:
        s = ''
        for letter in s_list:
            s += letter
        return s


print(superReducedString('abbaca'))
