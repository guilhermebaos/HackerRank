# https://www.hackerrank.com/challenges/hackerland-radio-transmitters/problem


def hackerlandRadioTransmitters(x, k):
    # Sort the positions of the houses and make their locations unique
    x = list(set(x))
    x.sort()

    # Get the number os transmiters
    num_t = 0
    while len(x) > 0:
        subset_x = x[0:1 + 2 * k]       # Maximum subset of houses that are possibly covered for this transmitter

        start = x[0]                    # First house the transmitter needs to cover

        # Where the transmitter is, in order to cover the first house but be as far away from it as possible
        # in order to cover more of the houses that come next
        for transmitter in range(start + k, start - 1, -1):
            if transmitter in subset_x:
                break

        # Where the last house covered is
        if subset_x[-1] < transmitter + k:  # Is the last possible house to be covered is in range, that's the end house
            end_index = len(subset_x) - 1
        else:                               # Otherwise, find the furthest away house still in range
            for end in range(transmitter + k, transmitter - 1, -1):
                if end in subset_x:
                    print(transmitter + k, end)
                    break
            end_index = subset_x.index(end)

        # The array of the houses still not covered
        x = x[end_index + 1:]
        num_t += 1

    return num_t
