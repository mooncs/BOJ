# ACM 호텔
T = int(input())
answer = ''
for _ in range(T):
    # 호텔의 층수 H, 각 층의 방 수 W, N번째 손님
    H, W, N = map(int, input().split())
    # 1층의 호텔인 경우
    if H == 1:
        answer = f'10{N}' if N//H<10 else f'1{N}'
    # 손님이 꼭대기 층에 머물 경우
    elif N%H == 0:
        answer = f'{H}0{N//H}' if N//H<10 else f'{H}{N//H}'
    # 나머지 경우
    else:
        answer = f'{N%H}0{N//H+1}' if N//H<9 else f'{N%H}{N//H+1}'
    
    print(answer)