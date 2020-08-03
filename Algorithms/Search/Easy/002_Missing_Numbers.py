def missingNumbers(arr, brr):
    all_nums = list(set(brr))

    arr_freq = []
    brr_freq = []

    for _ in range(len(all_nums)):
        arr_freq += [0]
        brr_freq += [0]

    for pos, num in enumerate(all_nums):
        arr_freq[pos] = arr.count(num)
        brr_freq[pos] = brr.count(num)

    missing = []
    for a_pair, b_num in zip(enumerate(arr_freq), brr_freq):
        a_num = a_pair[1]
        if a_num != b_num:
            missing += [all_nums[a_pair[0]]]

    missing.sort()
    return missing
