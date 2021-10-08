# 이분 그래프
# bfs
# 메모리 51792KB, 시간 1756ms
import sys
from collections import deque

def bfs(v):
    global flag
    q = deque([v])
    check[v] = 1
    while flag and q:
        pos = q.popleft()
        for i in graph[pos]:
            if check[i] and check[i]==check[pos]:
                flag = False
                return
            if not check[i]:
                q.append(i)
                check[i] = check[pos]*-1

for _ in range(int(sys.stdin.readline())):
    v, e = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(v+1)]
    check = [0]*(v+1)

    for _ in range(e):
        x, y = map(int, sys.stdin.readline().split())
        graph[x].append(y)
        graph[y].append(x)

    flag = True
    for i in range(1, v+1):
        if not check[i]:
            bfs(i)
        if not flag:break
    print('YES' if flag else 'NO')   


# # 시간 초과
# from collections import deque
# def bfs(v):
#     global flag
#     q = deque()
#     q.append(v)
#     check[v] = 1
#     while q:
#         pos = q.popleft()
#         for i in graph[pos]:
#             if check[i] and check[i]==check[pos]:
#                 return False
#             if not check[i]:
#                 q.append(i)
#                 check[i] = check[pos]*-1
#     return True

# for _ in range(int(input())):
#     v, e = map(int, input().split())
#     graph = [[] for _ in range(v+1)]
#     check = [0]*(v+1)

#     for _ in range(e):
#         x, y = map(int, input().split())
#         graph[x].append(y)
#         graph[y].append(x)

#     flag = True
#     for i in range(1, v+1):
#         if not check[i] and not bfs(i):
#             print('NO')
#             break
#     else:print('YES')


# 런타임 에러 (RecursionError) => sys.setrecursionlimit(100000)
# 메모리 62936KB, 시간 1660ms
import sys 
sys.setrecursionlimit(100000)
def dfs(v, chk):
    global flag
    check[v] = chk
    if not flag:
        return
    for i in graph[v]:
        if check[i] == chk:
            flag = False
            return
        elif not check[i]:
            dfs(i, -chk)
    
for _ in range(int(sys.stdin.readline())):
    v, e = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(v+1)]
    check = [0]*(v+1)

    for _ in range(e):
        x, y = map(int, sys.stdin.readline().split())
        graph[x].append(y)
        graph[y].append(x)

    flag = True
    for i in range(1, v+1):
        if not check[i]:
            dfs(i, 1)
        if not flag:break
    print('YES' if flag else 'NO')


# # 시간 초과
# def dfs(v, chk):
#     global flag
#     check[v] = chk
#     if not flag:
#         return
#     for i in graph[v]:
#         if check[i] == chk:
#             flag = False
#             return
#         elif not check[i]:
#             dfs(i, -chk)
    
# for _ in range(int(input())):
#     v, e = map(int, input().split())
#     graph = [[] for _ in range(v+1)]
#     check = [0]*(v+1)

#     for _ in range(e):
#         x, y = map(int, input().split())
#         graph[x].append(y)
#         graph[y].append(x)

#     flag = True
#     for i in range(1, v+1):
#         if not check[i]:
#             dfs(i, 1)
#         if not flag:break
#     print('YES' if flag else 'NO')


# # 실패
# def dfs(v, chk):
#     check[v] = chk
#     for i in graph[v]:
#         if check[i] == chk:
#             return 'NO'
#         elif not check[i]:
#             dfs(i, -chk)
    
# for _ in range(int(input())):
#     v, e = map(int, input().split())
#     graph = [[] for _ in range(v+1)]
#     check = [0]*(v+1)

#     for _ in range(e):
#         x, y = map(int, input().split())
#         graph[x].append(y)
#         graph[y].append(x)

#     for i in range(1, v+1):
#         if not check[i]:
#             result = dfs(i, 1)
#         if result:break
#     print(result if result else 'YES')