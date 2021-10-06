# 토마토
# 메모리 48488 KB 시간 3580 ms
import sys
from collections import deque

def chktoma():
    zcnt = 0
    for z in range(h):
        for y in range(n):
            for x in range(m):
                if tomato[z][y][x] == 1:
                    q.append((x, y, z))
                elif tomato[z][y][x] == 0:
                    zcnt += 1
    if zcnt == 0:
        return False
    return True

def bfs():
    dxyz = [[-1,0,0],[1,0,0],[0,-1,0],[0,1,0],[0,0,-1],[0,0,1]]
    while q:
        x, y, z = q.popleft()
        for i in range(6):
            dx = x + dxyz[i][0]
            dy = y + dxyz[i][1]
            dz = z + dxyz[i][2]
            if 0<=dx<m and 0<=dy<n and 0<=dz<h and tomato[dz][dy][dx] == 0:
                q.append((dx, dy, dz))
                tomato[dz][dy][dx] = tomato[z][y][x] + 1
            
# 가로 m, 세로 n, 높이 h
m, n, h = map(int, sys.stdin.readline().split())
tomato = [[list(map(int, sys.stdin.readline().split())) for _ in range(n)] for _ in range(h)]
q= deque()
chk = chktoma()
if chk:
    bfs()
    zcnt = 0
    maxcnt = 0
    for toma in tomato:
        for t in toma:
            zcnt += t.count(0)
            if maxcnt < max(t):
                maxcnt = max(t)
        if zcnt:
            print(-1)
            break
    else:print(maxcnt-1)
else:
    print(0)


# # 메모리 48444 KB 시간 3924 ms
# import sys
# from collections import deque

# def bfs():
#     dxyz = [[-1,0,0],[1,0,0],[0,-1,0],[0,1,0],[0,0,-1],[0,0,1]]
#     while q:
#         x, y, z = q.popleft()
#         for i in range(6):
#             dx = x + dxyz[i][0]
#             dy = y + dxyz[i][1]
#             dz = z + dxyz[i][2]
#             if 0<=dx<m and 0<=dy<n and 0<=dz<h and tomato[dz][dy][dx] == 0:
#                 q.append((dx, dy, dz))
#                 tomato[dz][dy][dx] = tomato[z][y][x] + 1
            
# # 가로 m, 세로 n, 높이 h
# m, n, h = map(int, sys.stdin.readline().split())
# tomato = [[list(map(int, sys.stdin.readline().split())) for _ in range(n)] for _ in range(h)]
# q= deque()
# for z in range(h):
#     for y in range(n):
#         for x in range(m):
#             if tomato[z][y][x] == 1:
#                 q.append((x, y, z))
# bfs()
# zcnt = 0
# maxcnt = 0
# for toma in tomato:
#     for t in toma:
#         zcnt += t.count(0)
#         if maxcnt < max(t):
#             maxcnt = max(t)
#     if zcnt:
#         print(-1)
#         break
# else:
#     if maxcnt == 1:print(0)
#     else:print(maxcnt-1)