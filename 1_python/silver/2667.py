# 2667. 단지번호붙이기
import sys
from collections import deque

def bfs(r, c, color):
    drc = [[-1,0],[1,0],[0,-1],[0,1]]                   # 상하좌우
    visited[r][c] = color                               # 시작점 방문 표시
    q = deque()                                         # 큐 생성
    q.append((r, c))                                    # 시작점 인큐
    cnt = 0                                             # 카운팅 변수
    while q:                                            # 큐가 빌 때까지
        cr, cc = q.popleft()                            # 현 좌표 표시
        cnt += 1                                        # 집 수 +1
        for i in range(4):                              # 4방향 모두 방문
            dr = cr + drc[i][0]                         # 행 갱신
            dc = cc + drc[i][1]                         # 열 갱신
            if 0<=dr<n and 0<=dc<n:                     # 행과 열이 범위 내에 있고
                if apt[dr][dc] and not visited[dr][dc]: # 집이 존재하고 방문하지 않았다면
                    visited[dr][dc] = color             # 방문 표시
                    q.append((dr, dc))                  # 큐에 현재 집 좌표 인큐
    return cnt                                          # 현재 단지 집 수 반환

n = int(sys.stdin.readline())
apt = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
color = 1
answer = []
for i in range(n):
    for j in range(n):
        if apt[i][j] == 1 and not visited[i][j]:
            cnt = bfs(i, j, color)
            answer.append(cnt)
            color += 1
answer.sort()
print(len(answer))
print(*answer, sep='\n')

# ###################################################################
# # 상하좌우
# dr = [-1,1,0,0]
# dc = [0,0,-1,1]
# def BFS(r, c, color):
#     # Q선언과 동시 담아두고 방문 체크
#     Q = [(r,c)]
#     visited[r][c] = color
#     cnt = 0

#     while Q:
#         curr_r, curr_c = Q.pop(0)
#         cnt += 1    # 방문했으니, 카운트
#         for i in range(4):
#             nr = curr_r + dr[i]
#             nc = curr_c + dc[i]
#             # 범위를 벗어나면 continue
#             if nr<0 or nr>=N or nc<0 or nc>=N:continue
#             # 갈 수 있다면
#             if apt[nr][nc]==1 and visited[nr][nc] == 0:
#                 Q.append((nr,nc))
#                 visited[nr][nc] = color
#     return cnt

# def DFS(r,c):
#     global home_count
#     home_count += 1
#     visited[r][c] = color

#     for i in range(4):
#         nr = r + dr[i]
#         nc = c + dc[i]
#         # 범위를 벗어나면 continue
#         if nr<0 or nr>=N or nc<0 or nc>=N:continue
#         # 갈 수 있다면
#         if apt[nr][nc]==1 and visited[nr][nc] == 0:
#             DFS(nr, nc)



# # 단지 N*N
# N = int(input())

# apt = [list(map(int, input())) for _ in range(N)]

# visited = [[0]*N for _ in range(N)]

# ans = []
# color = 1
# # 아파트 단지 전체 순회하면서 넘버링
# for i in range(N):
#     for j in range(N):
#         if apt[i][j] == 1 and visited[i][j] == 0:
#             # DFS
#             home_count = 0
#             tmp = DFS(i, j)
#             ans.append(home_count)
#             # # BFS
#             # tmp = BFS(i, j, color)
#             # ans.append(tmp)
#             color += 1
#             for a in visited:
#                 print(*a)
#             print("-----------------------------------------")
            
# print(len(ans))
# for i in ans:
#     print(i)