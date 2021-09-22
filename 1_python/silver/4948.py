# 베르트랑 공준
# 최대 n 123456까지의 소수를 미리 계산
N = 123456 * 2
# 소수를 체크할 리스트 생성
prime = [False, False] + [True] * (N-1)
for i in range(2, int(N**0.5)+1):
    if prime[i]:
        for j in range(2*i, N+1, i):
            prime[j] = False
while True:
    n = int(input())
    cnt = 0
    # 0이면 반복문 종료
    if n == 0:
        exit()
    # 1이면 1을 출력하고 반복문 처음으로
    elif n == 1:
        print(1)
        continue
    # 0과 1이 아닐 경우
    else:
        # 해당 수가 소수이면 카운트한다.
        for i in range(n+1, 2*n+1):
            if prime[i]:
                cnt += 1
    print(cnt)

# # 시간 초과
# while True:
#     n = int(input())
#     cnt = 0
#     if n == 0:
#         exit()
#     elif n == 1:
#         print(1)
#         continue
#     else:
#         for i in range(n+1, 2*n+1):
#             for j in range(2, int(i ** 0.5)+1):
#                 if i % j == 0:
#                     break
#             else:
#                 cnt += 1
#     print(cnt)


# # 시간 초과
# def prime_num(x):
#     if x == 1:
#         return 0     
#     for i in range(2, int(x ** 0.5)+1):
#         if x % i == 0:
#             return 0
#     return 1

# while True:
#     n = int(input())
#     cnt = 0
#     if not n:
#         exit()
#     for i in range(n+1, 2*n+1):
#         cnt += prime_num(i)
#     print(cnt)