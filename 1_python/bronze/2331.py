# 분해합
# # 1572ms
# n = int(input())
# for i in range(1, n):
#     ds = i + sum(list(map(int, str(i))))
#     if ds == n:
#         print(i)
#         break
# else:
#     print(0)

# 시간 최적화, 68ms
n = int(input())
# n = 216
# 생성자최소값 = 216 - (a+b+c)
# a, b, c에 어떤 값이 올지는 모르지만 최대값인 9를 넣어서 계산하면 최소 생성자가 나온다.
min_n = max(0, n - len(str(n))*9)
for i in range(min_n, n):
    ds = i + sum(list(map(int, str(i))))
    if ds == n:
        print(i)
        break
else:
    print(0)
