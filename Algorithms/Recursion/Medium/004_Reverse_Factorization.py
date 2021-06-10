# https://www.hackerrank.com/challenges/k-factorization/problem

def build_up_to_n(n, A, current_states):
    state = current_states[-1]
    if state == n:
        yield current_states
    for index, multiple in enumerate(A):
        yield from build_up_to_n(n, A[index + 1:], current_states + [state * multiple])



def kFactorization(n, A):
    # Filter the list to only the divisors os n
    A = [a for a in A if n % a == 0]
    A.sort()
    if len(A) == 0:
        return -1
    factorization_generator = build_up_to_n(n, A, [1])
    try:
        return next(factorization_generator)
    except StopIteration:
        return -1


print(kFactorization(72, [2, 4, 6, 9, 3, 7, 16, 10, 5]))
print(kFactorization(175840877, [4, 5, 6, 7, 8, 10, 12, 17, 18, 19]))
