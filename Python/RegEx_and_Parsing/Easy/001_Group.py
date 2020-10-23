import re

string = input()

reg_ex = r'([A-Za-z0-9])\1+'

try:
    result = re.findall(reg_ex, string)[0]
    print(result)
except IndexError:
    print(-1)
