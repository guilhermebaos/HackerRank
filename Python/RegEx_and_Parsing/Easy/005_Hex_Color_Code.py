import re

reg_ex6digits = r'#[0-9a-fA-F]{5}[0-9a-fA-F](?=[:;,)])'
reg_ex3digits = r'#[0-9a-fA-F]{2}[0-9a-fA-F](?=[:;,)])'

n = int(input())
for _ in range(n):
    css_line = input()

    results = re.findall(reg_ex6digits, css_line)
    results += re.findall(reg_ex3digits, css_line)

    for res in results:
        print(res)
