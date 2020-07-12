def insertionSort1(n, arr):
    insert = arr[-1]
    for index in range(n - 1, -1, -1):
        if arr[index - 1] > insert:
            if index == 0:
                arr[index] = insert
            else:
                arr[index] = arr[index - 1]
            for num in arr:
                print(num, end=' ')
            print('')
        else:
            arr[index] = insert
            for num in arr:
                print(num, end=' ')
            break


insertionSort1(10, [2, 3, 4, 5, 6, 7, 8, 9, 10, 1])
