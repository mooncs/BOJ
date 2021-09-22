# 부녀회장이 될테야
T = int(input())
# 빈 아파트 만들기
apt = [[0]*15 for _ in range(15)]
# 아파트 인원 수 채우기
# 0층의 i호에는 i명이 산다.
for i in range(1, 15):
    apt[0][i] = i
# k층 n호에는 k-1층 n호의 사람과 k층 n-1호의 사람들의 합만큼 산다.
for r in range(1, 15):
    for c in range(1, 15):
        apt[r][c] = apt[r-1][c] + apt[r][c-1]

for _ in range(T):
    k = int(input())
    n = int(input())
    print(apt[k][n])


# # 2
# floor = int(input())
# num = int(input())
# arr = [x for x in range(1, num+1)]
# for  k in range(floor):
#     for i in range(1, num):
#         arr [i] += arr
# print(arr[-1])

