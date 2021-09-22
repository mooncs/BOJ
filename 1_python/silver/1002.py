# 터렛
# 원과 원의 교점의 개수 구하는 법 활용
T = int(input())
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    # 좌표 (x1, y1)와 좌표 (x2, y2)의 거리
    d = ((x2-x1)**2 + (y2-y1)**2)**0.5
    if d==0:
        if r1==r2:
            print(-1)
        else:
            print(0)
    else:
        if d == r1+r2 or d == abs(r2-r1):
            print(1)
        elif d < r1+r2 and d > abs(r2-r1):
            print(2)
        else:
            print(0)
