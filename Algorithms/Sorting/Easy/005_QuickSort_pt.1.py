def quickSort(arr):
    n = len(arr)
    pivot = arr[0]
    new_arr = [pivot]
    pivot_index = 0
    equal_len = 0
    for num in arr[1:]:
        if num < pivot:
            new_arr.insert(pivot_index - equal_len, num)
            pivot_index += 1
        elif num > pivot:
            new_arr.insert(n, num)
        else:
            new_arr.insert(pivot_index + 1, num)
            equal_len += 1
    return new_arr


"""
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

    new_arr = []
    for l in left:
        new_arr += [l]
    for e in equal:
        new_arr += [e]
    for r in right:
        new_arr += [r]

    return new_arr
"""
