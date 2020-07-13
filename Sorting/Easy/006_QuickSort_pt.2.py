def quickSort(arr):
    pivot = arr[0]
    left, equal, right = [], [], []
    for num in arr:
        if num < pivot:
            left += [num]
        elif num == pivot:
            equal += [num]
        else:
            right += [num]

    if len(left) > 1:
        left = quickSort(left)
    if len(right) > 1:
        right = quickSort(right)

    for num in left:
        print(num, end=' ')
    for num in equal:
        print(num, end=' ')
    for num in right:
        print(num, end=' ')

    print('')
    return left + equal + right


print(quickSort([5, 8, 3, 2, 1, 0, 9, 10]))
