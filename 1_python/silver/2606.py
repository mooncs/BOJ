# 바이러스
import sys
from collections import deque

def bfs(x):
    q = deque(connection[x])        # 1과 연결된 컴퓨터 추가
    virus[x] = 1                    # 1번 컴퓨터 방문 표시
    while q:                        # q과 빌 때까지 반복
        p = q.popleft()             # 첫 번째 요소를 뽑고
        if virus[p]:continue        # 해당 컴퓨터를 방문했으면 다음 컴퓨터 탐색
        virus[p] = 1                # 미방문 컴퓨터 방문 표시
        if connection[p]:           # 해당 컴퓨터와 연결된 컴퓨터가 있으면
            for c in connection[p]:
                q.append(c)         # 해당 컴퓨터를 q에 인큐
    
n = int(sys.stdin.readline())
connection = [[] for _ in range(n+1)]
virus = [0]*(n+1)
for _ in range(int(sys.stdin.readline())):
    s, e = map(int, sys.stdin.readline().split())
    # 방향이 없다.
    connection[s].append(e)
    connection[e].append(s)
bfs(1)
print(sum(virus)-1)

# # 틀렸습니다.
# # 양방향 체크를 하지 않았음
# import sys
# from collections import deque

# def bfs(x):
#     q = deque(connection[x])
#     virus[x] = 1
#     while q:
#         p = q.popleft()
#         if virus[p]:continue
#         virus[p] = 1
#         if connection[p]:
#             for c in connection[p]:
#                 q.append(c)
    
# n = int(sys.stdin.readline())
# connection = [[] for _ in range(n+1)]
# virus = [0]*(n+1)
# for _ in range(int(sys.stdin.readline())):
#     s, e = map(int, sys.stdin.readline().split())
#     connection[s].append(e)
# bfs(1)
# print(sum(virus)-1)