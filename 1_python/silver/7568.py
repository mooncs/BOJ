# 덩치
# # 1, 76ms
# n = int(input())
# people = [list(map(int, input().split())) for _ in range(n)]
# rank = [0]*n
# for i in range(n):
#     idx = (i+1)%n
#     while i != idx:
#         # 자신보다 덩치가 큰 사람의 수를 구한다.
#         if people[i][0] < people[idx][0] and people[i][1] < people[idx][1]:
#             rank[i] += 1
#         idx = (idx+1)%n
#     # 자신보다 덩치가 큰 사람의 수에다 1을 더하면 자신의 등수가 된다.
#     rank[i] += 1

# print(*rank)


# 68ms
n = int(input())
people = [list(map(int, input().split())) for _ in range(n)]
rank = [1]*n
for i in range(n):
    idx = (i+1)%n
    while i != idx:
        # 자신보다 덩치가 큰 사람의 수를 구한다.
        if people[i][0] < people[idx][0] and people[i][1] < people[idx][1]:
            rank[i] += 1
        idx = (idx+1)%n

print(*rank)


# # 2, 76ms
# n = int(input())
# people = [list(map(int, input().split())) for _ in range(n)]
# for i in people:
#     rank = 1
#     for j in people:
#         if i[0] < j[0] and i[1] < j[1]:
#             rank += 1
#     print(rank, sep=' ')