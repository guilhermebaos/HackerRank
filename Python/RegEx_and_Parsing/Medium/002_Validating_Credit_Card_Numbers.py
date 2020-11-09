import re

reg_ex_main = r'^[456]\d{3}-?\d{4}-?\d{4}-?\d{4}(?=$)'
reg_ex_copies = r'(\d)\1{3}'

n = int(input())

for _ in range(n):
    cc_number = input()
    if re.search(reg_ex_main, cc_number) and not re.search(reg_ex_copies, cc_number.replace('-', '')):
        print('Valid')
    else:
        print('Invalid')
