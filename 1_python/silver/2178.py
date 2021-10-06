# 미로 탐색
import sys

def dfs():
    drc = [[-1,0],[1,0],[0,-1],[0,1]]   # 상하좌우
    st = [(0,0,1)]
    maze[0][0] = 0
    result = 10000
    while st:
        r, c, cnt = st.pop()
        if r == n-1 and c == m-1:
            if cnt < result:
                result = cnt
            maze[n-1][m-1] = '1'
            continue
        for i in range(4):
            dr = r + drc[i][0]
            dc = c + drc[i][1]
            if 0<=dr<n and 0<=dc<m and maze[dr][dc]=='1':
                maze[dr][dc] = 0
                st.append((dr,dc, cnt+1))
    return result

# 세로 n, 가로 m
n, m = map(int, sys.stdin.readline().split())
maze = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
print(dfs())
