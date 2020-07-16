A = set(input().split())

result = True
n = int(input())
for _ in range(n):
    B = set(input().split())
    if A.intersection(B) == B and len(B) < len(A):
        pass
    else:
        result = False

print(result)