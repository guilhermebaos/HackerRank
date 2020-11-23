import re
from email.utils import parseaddr

reg_ex = r'[a-zA-Z0-9][\w\-\.]{1,}@[a-zA-Z]{1,}\.[a-zA-Z]{1,3}$'

n = int(input())

for _ in range(n):
    in_str = input()

    email_str = parseaddr(in_str)[1]

    if re.match(reg_ex, email_str):
        print(in_str)
