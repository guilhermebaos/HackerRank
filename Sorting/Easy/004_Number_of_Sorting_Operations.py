def runningTime(arr):
    shifts = 0
    for i in range(1, len(arr)):
        j = i - 1
        key = arr[i]
        while (j >= 0) and (arr[j] > key):
            arr[j + 1] = arr[j]
            shifts += 1
            j -= 1
        arr[j + 1] = key
    return shifts


print(runningTime([4, 4, 3, 4]))
