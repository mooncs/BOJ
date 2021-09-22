# 골드바흐의 추측
prime = [False, False] + [True] * (10000)
for i in range(2, int(10000**0.5)+1):
    if prime[i]:
        for j in range(2*i, 10001, i):
            prime[j] = False
T = int(input())
for _ in range(T):
    n = int(input())
    s, e = n//2, n//2
    while True:
        if prime[s] and prime[e]:
            print(s, e)
            break
        else:
            s -= 1
            e += 1

# # 시간 초과
# T = int(input())
# for _ in range(T):
#     n = int(input())
#     prime = [x for x in range(2, n)]
#     for i in range(2, int(n**0.5)+1):
#         if i in prime:
#             for j in range(2*i, n, i):
#                 if j in prime:
#                     prime.remove(j)
#     prime_sum = []
#     for i in range(len(prime)):
#         for j in range(len(prime)-1, i-1, -1):
#             if prime[i]+prime[j]==n:
#                 prime_sum.append((prime[i], prime[j]))
#     print(*prime_sum[-1])


# # 시간 초과
# T = int(input())
# prime = [x for x in range(2, 10001)]
# for i in range(2, int(10000**0.5)+1):
#     if i in prime:
#         for j in range(2*i, 10001, i):
#             if j in prime:
#                 prime.remove(j)

# for _ in range(T):
#     n = int(input())
#     prime_sum = []
#     for i in range(len(prime)):
#         if prime[i] > n:
#             break
#         for j in range(len(prime)-1, i-1, -1):
#             if prime[j] > n:
#                 continue
#             if prime[i]+prime[j]==n:
#                 prime_sum.append((prime[i], prime[j]))
#     print(*prime_sum[-1])