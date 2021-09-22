# Fly me to the Alpha Centauri
from math import sqrt
# 규칙은 풀이 노트 참고
T = int(input())
for _ in range(T):
    x, y = map(int, input().split())
    dist = y-x
    n = int(sqrt(dist))
    if dist <= 3:
        print(dist)
    elif dist == n** 2:
        print(2*n - 1)
    elif n**2 < dist <= n**2+n:
        print(2*n)
    else:
        print(2*(n+1) - 1)