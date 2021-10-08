# 벽 부수고 이동하기
import sys
from collections import deque
read = sys.stdin.readline

def bfs(r, c, cnt, destroy):
    global min_cnt
    drc = [[-1,0], [1,0], [0,-1], [0,1]]
    q = deque()
    q.append((r, c, cnt, destroy))
    while q:
        cr, cc, cnt, destroy = q.popleft()
        if min_cnt <= cnt:continue
        if cr == n-1 and cc == m-1:
            min_cnt = cnt
            break
        for i in range(4):
            mr = cr + drc[i][0]
            mc = cc + drc[i][1]
            if mr < 0 or mr >= n or mc < 0 or mc >= m:continue
            if visited[mr][mc]:continue
            if maze[mr][mc] == '0':
                visited[mr][mc] = 1
                q.append((mr, mc, cnt+1, destroy))
            elif destroy:
                dvisited[mr][mc] = 1
                q.append((mr, mc, cnt+1, False))

n, m = map(int, read().split())
maze = [list(read().rstrip()) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
dvisited = [[0]*m for _ in range(n)]
min_cnt = 1000000
bfs(0, 0, 1, True)
print(-1 if min_cnt==1000000 else min_cnt)


# 틀렸습니다.
import sys
from collections import deque
read = sys.stdin.readline

def bfs(r, c, cnt, destroy):
    global min_cnt
    drc = [[-1,0], [1,0], [0,-1], [0,1]]
    q = deque()
    q.append((r, c, cnt, destroy))
    while q:
        cr, cc, cnt, destroy = q.popleft()
        if min_cnt <= cnt:continue
        if cr == n-1 and cc == m-1:
            min_cnt = cnt
            break
        for i in range(4):
            mr = cr + drc[i][0]
            mc = cc + drc[i][1]
            if mr < 0 or mr >= n or mc < 0 or mc >= m:continue
            if visited[mr][mc]:continue
            if maze[mr][mc] == '0':
                visited[mr][mc] = 1
                q.append((mr, mc, cnt+1, destroy))
            if destroy:
                visited[mr][mc] = 1
                q.append((mr, mc, cnt+1, False))

n, m = map(int, read().split())
maze = [list(read().rstrip()) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
min_cnt = 1000000
bfs(0, 0, 1, True)
print(-1 if min_cnt==1000000 else min_cnt)


# # 런타임 에러 (RecursionError), 메모리 초과
# import sys
# sys.setrecursionlimit(100000)
# read = sys.stdin.readline

# def dfs(r, c, cnt, destroy):
#     global min_cnt
#     if min_cnt <= cnt:return

#     if r == n-1 and c == m-1:
#         min_cnt = cnt
#         return

#     drc = [[-1,0], [1,0], [0,-1], [0,1]]
#     for i in range(4):
#         mr = r + drc[i][0]
#         mc = c + drc[i][1]
#         if mr < 0 or mr >= n or mc < 0 or mc >= m:continue
#         if visited[mr][mc]:continue
#         if maze[mr][mc] == '0':
#             visited[mr][mc] = 1
#             dfs(mr, mc, cnt+1, destroy)
#             visited[mr][mc] = 0
#         elif destroy:
#             visited[mr][mc] = 1
#             dfs(mr, mc, cnt+1, False)
#             visited[mr][mc] = 0

# n, m = map(int, read().split())
# maze = [list(read().rstrip()) for _ in range(n)]
# visited = [[0]*m for _ in range(n)]
# min_cnt = 1000000
# dfs(0, 0, 1, True)
# print(-1 if min_cnt==1000000 else min_cnt)