# https://www.hackerrank.com/challenges/3d-surface-area/problem?isFullScreen=true

def surfaceArea(A):
    total = 0
    y_max, x_max = len(A), len(A[0])

    # Sum the z surface area, because the blocks are vertically stacked,
    # there are always 2 units of surface area exposed per (x, y) coordinate on the base
    total += 2 * x_max * y_max

    for y in range(y_max):
        for x in range(x_max):
            z_max = A[y][x]
            for z in range(z_max):
                print(x, y, z, total)
                if y == 0 or A[ y -1][x] < z + 1:
                    total += 1
                if y == y_max - 1 or A[ y +1][x] < z + 1:
                    total += 1
                if x == 0 or A[y][ x -1] < z + 1:
                    total += 1
                if x == x_max - 1 or A[y][ x +1] < z + 1:
                    total += 1

    return total
