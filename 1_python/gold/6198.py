# 6198. 옥상 정원 꾸미기
import sys

n = int(input())
h = [int(input()) for _ in range(n)]

# n = int(sys.stdin.readline().rstrip())
# h = [int(sys.stdin.readline().rstrip()) for _ in range(n)]

stack = [h[0]]
total = 0
for i in range(1, n):
    if stack[-1] <= h[i]:
        while stack and stack[-1] <= h[i]:
            stack.pop()
        stack.append(h[i])
    else:
        stack.append(h[i])

    total += len(stack)-1
print(total)
        

# # 시간초과
# import sys
# # 빌딩의 개수 n
# # n = int(input())
# n = int(sys.stdin.readline().rstrip())
# # 각 빌딩의 층수 받기
# h = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
# # 옥상정원을 확인할 수 있는 총 수, total
# total = 0
# for i in range(n-1):
#     # 각 빌딩에서 확인할 수 있는 옥상정원 수, cnt
#     cnt = 0
#     for j in range(i+1, n):
#         if h[i] > h[j]:
#             cnt += 1
#         else:
#             break
#     total += cnt

# print(total)
