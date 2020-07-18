def closestNumbers(arr):
    arr = quickSort(arr)

    mini = abs(arr[1] - arr[0])
    differences = []
    for index in range(len(arr) - 1):
        diff = arr[index + 1] - arr[index]
        if diff < 0:
            diff *= -1
        differences += [diff]
        if diff < mini:
            mini = diff

    result = []
    for pos, diff in enumerate(differences):
        if diff == mini:
            result += [arr[pos], arr[pos + 1]]

    return result


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
    return left + equal + right


print(closestNumbers([5, 4, 3, 2]))
