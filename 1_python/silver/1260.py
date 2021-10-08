import sys
from collections import deque
read = sys.stdin.readline

def dfs(v):
    for x in connect[v]:
        if not dvisited[x]:
            dvisited[x] = 1
            dresult.append(str(x))
            dfs(x)

def bfs(v):
    q = deque([v])
    while q:
        pos = q.popleft()
        bresult.append(pos)
        for x in connect[pos]:
            if not bvisited[x]:
                bvisited[x]=1
                q.append(x)
    
# 정점의 개수 n, 간선의 개수 m, 탐색 시작 정점 번호 v
n, m, v = map(int, read().split())
connect = [[] for _ in range(n+1)]
dvisited, bvisited = [0]*(n+1), [0]*(n+1)
dvisited[v], bvisited[v] = 1, 1
dresult, bresult = [str(v)], []
for _ in range(m):
    x, y = map(int, read().split())
    connect[x].append(y)
    connect[y].append(x)
for c in connect:c.sort()
dfs(v)
print(*dresult)
bfs(v)
print(*bresult)