# 좌표 정렬하기
import sys
# sorted()활용, 아이템 각 요소들도 오름차순으로 정렬해준다.
# n = int(input())
n = int(sys.stdin.readline().rstrip())
answer = []
for _ in range(n):
    # x, y = map(int, input().split())
    x, y = map(int, sys.stdin.readline().rstrip().split())
    answer.append((x, y))
for a in sorted(answer):
    print(*a)

# # sort()와 lambda 활용
# # n = int(input())
# n = int(sys.stdin.readline().rstrip())
# answer = []
# for _ in range(n):
#     # x, y = map(int, input().split())
#     x, y = map(int, sys.stdin.readline().rstrip().split())
#     answer.append((x, y))
# answer.sort(key=lambda x: (x[0], x[1]))
# for a in answer:
#     print(*a)