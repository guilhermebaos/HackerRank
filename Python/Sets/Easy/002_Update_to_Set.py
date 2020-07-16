len_A = int(input())
A = set(input().split())

N = int(input())
for _ in range(N):
    command = input().split()[0]
    B = set(input().split())
    if command == 'update':
        A.update(B)
    elif command == 'intersection_update':
        A.intersection_update(B)
    elif command == 'symmetric_difference_update':
        A.symmetric_difference_update(B)
    elif command == 'difference_update':
        A.difference_update(B)

A = list(map(int, A))

print(sum(A))
