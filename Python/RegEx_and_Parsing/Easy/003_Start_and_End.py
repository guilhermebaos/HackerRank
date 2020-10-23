import re

string = input()
match = input()

removed = 0
while True:
    m = re.search(match, string)
    if not m:
        if removed == 0:
            print((-1, -1))
        break

    pair = (m.start() + removed, m.end() - 1 + removed)
    string = string[m.start() + 1:]
    removed += m.start() + 1
    print(pair)
