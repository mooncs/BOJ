# 소수 구하기
def prime_num(x):
    if x == 1:
        return 0     
    for i in range(2, int(x ** 0.5)+1):
        if x % i == 0:
            return 0
    return x
    
M, N = map(int, input().split())
for x in range(M, N+1):
    if prime_num(x):
        print(x)