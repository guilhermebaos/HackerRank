# https://www.hackerrank.com/challenges/pairs/problem


def pairs(k, arr):
    # Sort the array
    arr.sort()

    # Number of pairs with difference k
    pairs_num = 0

    # Array with the differences between every consecutive values
    # Because the array is sorted, all differences are greater or equal to 0
    arr_difs = []
    for index, num in enumerate(arr[:-1]):
        arr_difs += [arr[index + 1] - num]

    # Create a 'Worm' that grows when the difference is smaller than k and shrinks when it's greater or equal to k
    start = 0
    end = 1
    len_arr_difs = len(arr_difs)
    while end <= len_arr_difs:
        total_diff = abs(sum(arr_difs[start:end]))
        if total_diff == k:
            pairs_num += 1
            start += 1
        elif total_diff > k:
            start += 1
        else:
            end += 1
    return pairs_num


k1 = int(input())
arr1 = list(map(int, input().rstrip().split()))

print(pairs(k1, arr1))
