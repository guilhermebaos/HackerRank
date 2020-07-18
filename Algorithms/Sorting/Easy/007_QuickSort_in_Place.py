n = int(input())
array = list(map(int, input().split()))

def quickSort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quickSort(arr, low, pivot_index - 1)
        quickSort(arr, pivot_index + 1, high)

    return arr


def partition(arr, low, high):
    pivot = arr[high]
    i = low
    j = low
    for j in range(low, high):
        if arr[j] < pivot:
            temp = arr[j]
            arr[j] = arr[i]
            arr[i] = temp
            i += 1
    arr[high] = arr[i]
    arr[i] = pivot
    print_list(arr)
    return i


def print_list(arr):
    for item in arr:
        print(item, end=' ')
    print('')


quickSort(array, 0, len(array) - 1)



'''
def partition_Hoare(arr, low, high):
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
'''
