import re

T = int(input())
reg_ex1 = r'\.\d+'
reg_ex2 = r'[+-]?\.\d+'
reg_ex3 = r'[+-]?\d+\.\d+'

for _ in range(T):
    N = input()
    m1 = re.match(reg_ex1, N)
    m2 = re.match(reg_ex2, N)
    m3 = re.match(reg_ex3, N)

    try:
        float(N)
        if m1 or m2 or m3:
            print('True')
        else:
            print('False')
    except ValueError:
        print('False')
