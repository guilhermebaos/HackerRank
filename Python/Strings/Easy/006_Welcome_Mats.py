N, M = map(int, input().split())

pattern = '.|.'

# Top Half
for row in range(N // 2):
    print((pattern * (row * 2 + 1)).center(M, '-'))

# Welcome
print('WELCOME'.center(M, '-'))

# Bottom Half
for row in range(N // 2, 0, -1):
    print((pattern * (row * 2 - 1)).center(M, '-'))
