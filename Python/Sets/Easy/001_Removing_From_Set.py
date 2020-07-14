n = int(input())
original_set = set(map(int, input().split()))

n_c = int(input())
for _ in range(n_c):
    command = input().split()
    if command[0] == 'pop':
        original_set.pop()
    elif command[0] == 'remove':
        original_set.remove(int(command[1]))
    elif command[0] == 'discard':
        original_set.discard(int(command[1]))

print(sum(original_set))
