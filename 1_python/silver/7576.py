# 토마토
# 메모리 98848 KB 시간 2336 ms
import sys
from collections import deque

def bfs():
    drc = [[-1,0],[1,0],[0,-1],[0,1]]
    while q:
        r, c = q.popleft()
        for i in range(4):
            dr = r + drc[i][0]
            dc = c + drc[i][1]
            if 0<=dc<m and 0<=dr<n and tomato[dr][dc] == 0:
                q.append((dr, dc))
                tomato[dr][dc] = tomato[r][c] + 1
            
# 가로 m, 세로 n
m, n = map(int, sys.stdin.readline().split())
tomato = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
q= deque()
zcnt = 0
for r in range(n):
    for c in range(m):
        if tomato[r][c]== 1:
            q.append((r, c))
    zcnt += tomato[r].count(0)
if zcnt:
    bfs()
    zcnt = 0
    maxcnt = 0
    for toma in tomato:
        zcnt += toma.count(0)
        if maxcnt < max(toma):
            maxcnt = max(toma)
        if zcnt:
            print(-1)
            break
    else:print(maxcnt-1)
else:
    print(0)