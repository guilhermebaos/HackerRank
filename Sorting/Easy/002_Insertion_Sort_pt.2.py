def sort_last_num(arr):
    n = len(arr)
    insert = arr[-1]
    for index in range(n - 1, -1, -1):
        if arr[index - 1] > insert:
            if index == 0:
                arr[index] = insert
            else:
                arr[index] = arr[index - 1]
        else:
            arr[index] = insert
            break
    return arr


def insertionSort2(n, arr):
    for index in range(0, n):
        sorted_arr = sort_last_num(arr[0:index + 1])
        arr[0:index + 1] = sorted_arr
        if index != 0:
            for num in arr:
                print(num, end=' ')
            print('')


print(insertionSort2(7, [3, 4, 7, 5, 6, 2, 1]))