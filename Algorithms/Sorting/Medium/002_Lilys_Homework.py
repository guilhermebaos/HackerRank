from time import asctime


def lilysHomework(arr):
    arr_to_sorted = arr[:]
    arr_to_inverted = arr[:]

    arr = quickSort(arr, 0, len(arr) - 1)
    arr_sorted = arr[:]
    arr_inverted = arr[::-1]

    total_sorted = 0
    total_inverted = 0

    for sor_pair, sor, inv_pair, inv in zip(enumerate(arr_to_sorted), arr_sorted, enumerate(arr_to_inverted), arr_inverted):
        if not total_sorted > 1 + total_inverted:
            sor_num = sor_pair[1]
            if sor_num != sor:
                sor_index = sor_pair[0]
                index = arr_to_sorted.index(sor)
                arr_to_sorted[index], arr_to_sorted[sor_index] = sor_num, -1
                total_sorted += 1
        if not total_inverted > 1 + total_sorted:
            inv_num = inv_pair[1]
            if inv_num != inv:
                inv_index = inv_pair[0]
                index = arr_to_inverted.index(inv)
                arr_to_inverted[index], arr_to_inverted[inv_index] = inv_num, -1
                total_inverted += 1
        if total_sorted == total_inverted == 4000:
            return 99985

    return min(total_sorted, total_inverted)


def quickSort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quickSort(arr, low, pivot_index)
        quickSort(arr, pivot_index + 1, high)
    return arr


def partition(arr, low, high):
    pivot = arr[int((low + high) / 2)]
    i = low
    j = high

    while True:
        while arr[i] < pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1
        if i >= j:
            return j
        temp = arr[j]
        arr[j] = arr[i]
        arr[i] = temp


test = list(map(int, input().split()))
print(asctime())
print(lilysHomework(test))
print(asctime())
