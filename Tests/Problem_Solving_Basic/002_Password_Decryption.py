def decryptPassword(s):
    list_s = []
    for letter in s:
        list_s += [letter]

    i = len(s) - 1
    while True:
        if list_s[i] == '0':
            list_s[i] = list_s[0]
            list_s.pop(0)
            i -= 1
        elif list_s[i] == '*' and list_s[i - 1].islower() and list_s[i - 2].isupper():
            small = list_s[i - 1]
            list_s[i - 1] = list_s[i - 2]
            list_s[i - 2] = small
            list_s.pop(i)
            i -= 3
        else:
            i -= 1
        if i < 0:
            break

    return str(list_s).replace(', ', '').replace("'", '').replace('[', '').replace(']', '')


print(decryptPassword('51Pa*0Lp*0e'))


def encryptPassword(s):
    list_s = []
    for letter in s:
        list_s += [letter]

    i = 0
    while True:
        if list_s[i].isnumeric():
            list_s.insert(0, list_s[i])
            list_s[i + 1] = '0'
            i += 2
            if i >= len(list_s) - 2:
                break
        elif list_s[i].islower() and list_s[i + 1].isupper():
            small = list_s[i]
            list_s[i] = list_s[i + 1]
            list_s[i + 1] = small
            list_s.insert(i + 2, '*')
            i += 2
            if i >= len(list_s):
                break
        else:
            i += 1
            if i >= len(list_s):
                break

    return str(list_s).replace(', ', '').replace("'", '').replace('[', '').replace(']', '')


print(encryptPassword('aP1pL5e'))
