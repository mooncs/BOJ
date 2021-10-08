# 나이트의 이동
from collections import deque

def moving():
    dr = [-1, -2, -2, -1, 1, 2, 2, 1]
    dc = [2, 1, -1, -2, -2, -1, 1, 2]
    q = deque()
    q.append((sr,sc))
    chess[sr][sc] = 1
    while q:
        # 현 좌표
        cr, cc = q.popleft()
        # 목표 좌표에 도착하면
        if cr == gr and cc == gc:
            # 이동 횟수 출력, 시작을 1로 시작했기 때문에 -1
            return chess[cr][cc] - 1
        for i in range(8):
            # 좌표 이동
            mr = cr + dr[i]
            mc = cc + dc[i]
            # 좌표가 범위내에 있고, 방문하지 않았으면
            if 0<=mr<l and 0<=mc<l and not chess[mr][mc]:
                q.append((mr, mc))
                # 이동 횟수 카운트를 위해 이전 횟수 +1
                chess[mr][mc] = chess[cr][cc] + 1

for _ in range(int(input())):
    l = int(input())    # 체스판의 넓이는 l*l
    chess = [[0]*l for _ in range(l)]
    sr, sc = map(int, input().split())  # 시작 좌표
    gr, gc = map(int, input().split())  # 목표 좌표
    print(moving())