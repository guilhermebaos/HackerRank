def balancedSums(arr):
    left_sum = 0
    right_sum = sum(arr[1:])

    for pos in range(len(arr)):
        print(left_sum, right_sum)
        if left_sum == right_sum:
            return 'YES'
        else:
            left_sum += arr[pos]
            try:
                right_sum -= arr[pos + 1]
            except IndexError:
                break
    return 'NO'


print(balancedSums([1, 2, 3, 3]))
