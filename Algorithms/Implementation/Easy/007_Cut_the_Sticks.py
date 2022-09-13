# https://www.hackerrank.com/challenges/cut-the-sticks/problem?isFullScreen=true

def cutTheSticks(arr):
    lens = [len(arr)]
    while lens[-1] > 0:
        for _ in range(times := arr.count(mini := min(arr))):
            arr.remove(mini)
        lens += [lens[-1] - times]
    return lens[:-1]
