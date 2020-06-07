def staircase(n):
    for num_n in range(1, n+1):
        print(' ' * (n - num_n), end='')
        print('#' * (num_n))
