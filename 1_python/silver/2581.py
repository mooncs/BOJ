# 소수
def prime_num(x):
    # 1은 소수가 아님으로 0 반환
    if x == 1:
        return 0
    # 2~x-1까지 나누어 떨어지는 수가 있으면 소수가 아니므로 0 반환        
    for i in range(2, x):
        if x % i == 0:
            return 0
    # 소수면 x 반환
    return x

M = int(input())
N = int(input())
total, min_num = 0, 10000
for i in range(M, N+1):
    total += prime_num(i)
    if prime_num(i) and prime_num(i)<min_num:
        min_num = prime_num(i)
if not total:
    print(-1)
else:
    print(total, min_num, sep='\n')