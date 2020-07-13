def countingSort(arr):
    maxi = max(arr)

    counter = [0]
    for _ in range(0, maxi):
        counter += [0]

    for num in arr:
        counter[num] += 1

    sorted_arr = []
    for num, times in enumerate(counter):
        for _ in range(times):
            sorted_arr += [num]

    return sorted_arr

