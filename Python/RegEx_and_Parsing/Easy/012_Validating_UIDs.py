import re


def validate_UID(UID):
    if len(UID) != 10 or len(set(UID)) != len(UID):
        return False
    uppercase = 0
    numbers = 0
    for letter in UID:
        if not re.match(r'[A-Za-z0-9]', letter):
            return False
        if re.match(r'[0-9]', letter):
            numbers += 1
        elif re.match(r'[A-Z]', letter):
            uppercase += 1
    if uppercase >= 2 and numbers >= 3:
        return True
    return False


n = int(input())
for _ in range(n):
    if validate_UID(input()):
        print('Valid')
    else:
        print('Invalid')