import re

reg_ex = r' ([|&])\1(?= )'


def substitute(match):
    cond = match.group(0)
    if cond == ' &&':
        cond_text = ' and'
    elif cond == ' ||':
        cond_text = ' or'
    else:
        cond_text = cond
    return cond_text


n = int(input())
for _ in range(n):
    code_line = input()

    print(re.sub(reg_ex, substitute, code_line))
