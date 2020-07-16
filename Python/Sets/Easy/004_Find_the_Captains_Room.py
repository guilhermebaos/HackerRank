k = int(input())
rooms = list(input().split())

found1 = set()
found2 = set()
for n in rooms:
    print(n)
    set_n = {n}

    if found1.intersection(set_n) == set_n:
        found2.update(set_n)
    else:
        found1.update(set_n)

print(found1, found2)
print(list(found1.symmetric_difference(found2))[0])
