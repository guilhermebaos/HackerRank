def compareTriplets(a, b):
    a_points = 0
    b_points = 0
    for c in range(0, 3):
        if a[c] > b[c]:
            a_points += 1
        elif a[c] < b[c]:
            b_points += 1
    return [a_points, b_points]