def maxElement(n, maxSum, k):
    max_k = maxSum + 1
    left = k
    right = n - k - 1

    valid_left = min(left, max_k - 1)
    valid_right = min(right, max_k - 1)
    arr_sum = 0

    arr_sum += (max_k - 1 + max_k - valid_left) / 2 * valid_left
    arr_sum += left - valid_left
    arr_sum += (max_k - 1 + max_k - valid_right) / 2 * valid_right
    arr_sum += right - valid_right
    arr_sum += max_k

    while arr_sum > maxSum:
        max_k -= 1

        valid_left = min(left, max_k - 1)
        valid_right = min(right, max_k - 1)

        arr_sum -= n
        arr_sum += max(0, n - valid_left - valid_right - 1)

    return max_k


print(maxElement(3, 7, 1))
