# 유기농 배추
import sys
from collections import deque

def bfs(r, c, cnt):
    drc = [[-1,0],[1,0],[0,-1],[0,1]]   # 상하좌우
    visited[r][c] = 1                   # 시작점 방문 표시
    q = deque()                         # 큐 생성
    q.append((r, c))                    # 시작점 인큐
    while q:                            # 큐가 빌 때까지 
        cr, cc = q.popleft()            # 현 좌표 표시
        for i in range(4):              # 4방향 모두 방문
            dr = cr + drc[i][0]         # 행 이동
            dc = cc + drc[i][1]         # 열 이동
            # 행과 열이 범위안에 있고 배추가 존재하며 방문하지 않은 배추일 때
            if 0<=dr<n and 0<=dc<m and farm[dr][dc] and not visited[dr][dc]:
                q.append((dr, dc))      # 해당 좌표 인큐
                visited[dr][dc] = 1     # 해당 좌표 방문 표시

for _ in range(int(sys.stdin.readline())):
    # 가로 m, 세로 n, 위치 개수 k
    m, n, k = map(int, sys.stdin.readline().split())
    farm = [[0]*m for _ in range(n)]
    visited = [[0]*m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, sys.stdin.readline().split())
        farm[y][x] = 1
    cnt = 0
    for r in range(n):
        for c in range(m):
            if farm[r][c] == 1 and not visited[r][c]:
                bfs(r, c, cnt)
                cnt += 1
    print(cnt)