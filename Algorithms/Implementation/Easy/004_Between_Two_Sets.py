import math


def lcm(x, y):
    return abs(x * y) // math.gcd(x, y)


def primefact(n):
    i = 2
    factors = []
    while (i * i) <= n:
        if (n % i) == 0:
            n = n / i
            factors += [i]
        else:
            i += 1
            if i % 2 == 0:
                i += 1
            if i % 3 == 0 and i != 3:
                i += 1
        if n == 1:
            break
    if n > 1:
        factors += [int(n)]
    return factors


def num_divisors(n):
    if n == 1:
        return 1
    factors = primefact(n)
    organized = [[]]
    org = factors[0]
    for fact in factors:
        if fact == org:
            organized[-1] += [fact]
        else:
            organized += [[fact]]
            org = fact
    total = 1
    for fact_num in organized:
        total *= len(fact_num) + 1
    return total


def getTotalX(a, b):
    start = a[0]
    if len(a) != 1:
        for num in a[1:]:
            start = lcm(start, num)
    end = b[-1]
    if len(b) != 1:
        for num in b[::-1]:
            end = math.gcd(end, num)
    if end % start == 0:
        return num_divisors(end // start)
    else:
        return 0


la, lb = [2], [20, 30, 12]
print(getTotalX(la, lb))
