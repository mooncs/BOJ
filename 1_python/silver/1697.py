# 숨바꼭질
from collections import deque

def bfs():
    q = deque()
    q.append(n)
    while q:
        x = q.popleft()
        if x == k:
            return chk[x]
        for y in (x-1,x+1,x*2):
            if 0<=y<=100000 and not chk[y]:
                chk[y] = chk[x]+1
                q.append(y)

n, k = map(int, input().split())
chk = [0]*100001
print(bfs())


# # bfs미사용
# def find(n, k):
#     if n >= k:return n-k
#     elif k == 1:return 1
#     elif k%2:return min(find(n, k-1), find(n, k+1)) + 1
#     else:return min(k-n, find(n, k//2) + 1)
  
# n, k = map(int, input().split())
# print(find(n, k))


# # 메모리 초과
# from collections import deque

# def bfs():
#     q.append((n, 0))
#     while q:
#         x, cnt = q.popleft()
#         if x > 100000:continue
#         if x == k:
#             return cnt
#         q.append((x-1, cnt+1))
#         q.append((x+1, cnt+1))
#         q.append((x*2, cnt+1))

# n, k = map(int, input().split())
# q = deque()
# print(bfs())

