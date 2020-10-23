import re

string = input()

reg_ex = r'[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm][AEIOUaeiou][AEIOUaeiou]+(?=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])'

matches = re.findall(reg_ex, string)

if len(matches) == 0:
    print(-1)
else:
    for m in matches:
        print(m[1:])
