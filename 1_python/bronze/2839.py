# 설탕 배달
# 상근이는 사탕가게에 설탕을 정확하게 N킬로그램을 배달해야 한다.
N = int(input())
# 5로 나누어 떨어진다면, 
# 가장 작은 수의 봉투를 가져가는 것과 동일하기 때문에 더이상 계산 불필요
if N % 5 == 0:
    print(N//5)
# 3으로 나누어 떨어지는 경우,
# 3과 5를 섞어서 나누는 것보다 많은 수의 봉투를 가져갈 수도 있다.
else:
    answer = 0
    while True:
        # 3을 한 번씩 빼며
        N -= 3
        # 뺀 수가 음수이거나 1,2일 경우 정확히 나누어떨어지지 않으므로 -1 출력
        if 0< N < 3 or N<0:
            print(-1)
            break
        # 가져갈 봉투 수 1개 추가
        answer += 1
        # 이제 5로 나누어 떨어진다면,
        if N % 5 == 0:
            # 그 몫만큼 가져갈 봉투 수에 추가하고 종료
            answer += N//5
            print(answer)
            break