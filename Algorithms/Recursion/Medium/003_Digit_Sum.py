# https://www.hackerrank.com/challenges/recursive-digit-sum/problem


def superDigit(n, k=1):
    n = str(n)
    n_sum = sum(list(map(int, list(n)))) * k
    if len(str(n_sum)) > 1:
        return superDigit(n_sum)
    return n_sum


print(superDigit(123, 3))
