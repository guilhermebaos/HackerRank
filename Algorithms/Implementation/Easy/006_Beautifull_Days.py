# https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem?isFullScreen=true

def reverse_diff(n):
    n_lst = list(str(n))
    n_lst.reverse()
    return n - int(''.join(n_lst))


def beautifulDays(i, j, k):
    total = 0
    for day in range(i, j + 1):
        if reverse_diff(day) % k == 0:
            total += 1
    return total
