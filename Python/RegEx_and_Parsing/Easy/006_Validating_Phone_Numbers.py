import re

reg_ex = r'[789]\d{9}'

n = int(input())
for _ in range(n):
    number = input()
    if len(number) == 10:
        if re.match(reg_ex, number):
            print('YES')
        else:
            print('NO')
    else:
        print('NO')
