def breakingRecords(scores):
    maxi = scores[0]
    maxi_num = 0
    mini = scores[0]
    mini_num = 0
    for s in scores[1:]:
        if s > maxi:
            maxi = s
            maxi_num += 1
        elif s < mini:
            mini = s
            mini_num += 1
    return [maxi_num, mini_num]


print(breakingRecords([10, 5, 20, 20, 4, 5, 2, 25, 1]))