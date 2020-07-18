def bigSorting(unsorted): return quickSortBigStrings(unsorted)


def quickSortBigStrings(arr):
    if len(arr[:2]) <= 1:
        return arr

    pivot = arr[0]
    len_pivot = len(pivot)
    int_pivot = int(pivot)

    left, equal, right = [], [pivot], []
    for num in arr[1:]:
        len_num = len(num)
        if len_num > len_pivot:
            right += [num]
        elif len_num < len_pivot:
            left += [num]
        else:
            int_num = int(num)
            if int_num < int_pivot:
                left += [num]
            elif int_num > int_pivot:
                right += [num]
            else:
                equal += [num]

    left = quickSortBigStrings(left)
    right = quickSortBigStrings(right)
    return left + equal + right
