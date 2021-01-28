for i in range(1,int(input())+1):
    print(((10 ** i - 1) // 9) ** 2)

# Dumb Solution
for i in range(1,int(input())+1):
    print(int(10 ** (i - 1) + 10 ** (i - 2) + 10 ** (i - 3) + 10 ** (i - 4) + 10 ** (i - 5) + 10 ** (i - 6) + 10 ** (i - 7) + 10 ** (i - 8) + 10 ** (i - 9) + 10 ** (i - 10) + 10 ** (i - 11) + 10 ** (i - 12)) ** 2)
