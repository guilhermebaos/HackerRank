def miniMaxSum(arr):
    arr.sort()
    tot = 0
    for num in arr:
        tot += num
    print(tot-arr[4], tot-arr[0])
