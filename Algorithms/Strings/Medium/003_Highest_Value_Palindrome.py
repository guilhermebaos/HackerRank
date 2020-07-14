def highestValuePalindrome(s, n, k):
    s_list = []
    for letter in s:
        s_list += [letter]

    min_switch = 0
    for c in range(int(n / 2)):
        if s_list[c] != s_list[(n - 1) - c]:
            min_switch += 1

    if k < min_switch:
        return '-1'
    elif k == min_switch:
        for c in range(int(n / 2)):
            maximum = max(int(s_list[c]), int(s_list[(n - 1) - c]))
            if s_list[c] != s_list[(n - 1) - c]:
                s_list[c] = str(maximum)
                s_list[(n - 1) - c] = str(maximum)
        return join_list(s_list)
    else:
        extra_switch = k - min_switch
        if extra_switch == 1 and min_switch == 0:
            s_list[int(len(s_list) / 2)] = '9'
        else:
            for c in range(int(n / 2)):
                maximum = max(int(s_list[c]), int(s_list[(n - 1) - c]))
                if maximum != 9 and extra_switch > 0:
                    if s_list[c] == s_list[(n - 1) - c] and extra_switch > 1:
                        extra_switch -= 2
                    else:
                        extra_switch -= 1
                    s_list[c] = '9'
                    s_list[(n - 1) - c] = '9'
                elif s_list[c] != s_list[(n - 1) - c]:
                    s_list[c] = str(maximum)
                    s_list[(n - 1) - c] = str(maximum)
            if extra_switch > 0 and n % 2 == 1:
                s_list[int(len(s_list) / 2)] = '9'
        return join_list(s_list)


def join_list(li):
    s = ''
    for item in li:
        s += str(item)
    return s


string = '12321'
switches = 1
print(highestValuePalindrome(string, len(string), switches))
