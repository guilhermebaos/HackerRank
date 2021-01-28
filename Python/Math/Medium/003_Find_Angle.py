import math

AB, BC = int(input()), int(input())

MC = 0.5 * (AB ** 2 + BC ** 2) ** 0.5

alpha = math.atan(AB / BC)

BM = (BC ** 2 + MC ** 2 - 2 * BC * MC * math.cos(alpha)) ** 0.5

theta = math.degrees(math.asin(MC * math.sin(alpha) / BM))

if theta - int(theta) >= 0.5:
    print(str(int(theta + 1)) + '°')
else:
    print(str(int(theta)) + '°')
