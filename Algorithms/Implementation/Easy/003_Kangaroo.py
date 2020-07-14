def kangaroo(x1, v1, x2, v2):
    if x1 < x2 and v1 <= v2:
        return 'NO'
    a = (x2 - x1) / (v1 - v2)
    if int(a) == a:
        if a >= 0:
            return 'YES'
    return 'NO'


print(kangaroo(0, 3, 4, 2))
