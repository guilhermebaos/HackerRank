function getSecondLargest(nums) {
    let first = 0
    let second = 0
    let num

    for (let pos in nums) {
        num = nums[pos]
        if (num > first) {
            second = first
            first = num
        } else if (num > second && num < first) {
            second = num
        }
    }

    return second
}