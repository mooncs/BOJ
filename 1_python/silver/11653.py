# 소인수분해
# # 1
# N = int(input())
# i = 2
# while N > 1:
#     if N % i == 0:
#         print(i)
#         N //= i
#     else:
#         i += 1

# 2
n = int(input())
i = 2
r = int(n ** 0.5)
while i <= r:
    while not n % i:
        print(i)
        n //= i
    i += 1
if n > 1:
    print(n)