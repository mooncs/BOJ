# 소수 찾기
# 소수 찾기 함수 생성
def prime_num(x):
    # 1은 소수가 아님으로 0 반환
    if x == 1:
        return 0
    # 2~x-1까지 나누어 떨어지는 수가 있으면 소수가 아니므로 0 반환        
    for i in range(2, x):
        if x % i == 0:
            return 0
    # 그렇지 않으면 1 반환
    return 1

N = int(input())
nums = list(map(int, input().split()))
cnt = 0
for num in nums:
    cnt += prime_num(num)
print(cnt)