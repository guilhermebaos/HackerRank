n, m = input().split()
arr = list(input().split())
A = set(input().split())
B = set(input().split())


def happiness(array, happy_set, unhappy_set):
    h = 0
    for num in array:
        if happy_set.__contains__(num):
            h += 1
        elif unhappy_set.__contains__(num):
            h -= 1
    return h


print(happiness(arr, A, B))
