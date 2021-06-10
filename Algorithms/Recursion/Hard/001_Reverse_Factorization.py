# https://www.hackerrank.com/challenges/k-factorization/problem

# Construct the list of all states
def build_up_to_n(n, A, current_states):
    # Get latest state
    state = current_states[-1]

    # If it is the answer, return the result
    if state == n:
        yield current_states

    # If it is over the answer, return None (no answer this way)
    if state > n:
        yield None

    # If it is under the answer, keeping multipling the current state
    else:
        for index, multiple in enumerate(A):
            yield from build_up_to_n(n, A[index:], current_states + [state * multiple])


# Main function
def kFactorization(n, A):
    # Filter the list to only the divisors of n
    A = [a for a in A if n % a == 0]
    A.sort()
    if len(A) == 0:
        return -1

    # Initiate the generator
    factorization_generator = build_up_to_n(n, A, [1])

    # Find all the results
    all_results = []
    while True:
        try:
            result = next(factorization_generator)
            if result:
                all_results += [result]

        # When there are no more possible results
        except StopIteration:
            # If there is no way of forming the number, return -1
            if len(all_results) == 0:
                return -1

            # Of the possible results, return the first minimum length one
            else:
                len_results = list(map(len, all_results))
                min_len = min(len_results)
                all_results = [r for index, r in enumerate(all_results) if len_results[index] == min_len]
                return all_results[0]


print(kFactorization(72, [2, 4, 6, 9, 3, 7, 16, 10, 5]))
print(kFactorization(231000000, [2, 3, 5, 7, 11, 13, 17, 19]))
