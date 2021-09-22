# 체스판 다시 칠하기
# 4중 for문, 116ms
n, m = map(int, input().split())
board = [input() for _ in range(n)]
answer = 64
for i in range(n-7):
    for j in range(m-7):
        # 흰색으로 시작할 때, 검은색으로 시작할 때 2가지 경우 존재
        start_b, start_w = 0, 0
        for k in range(i, i+8):
            for l in range(j, j+8):
                # 행과 열의 합이 홀수일 때
                if (k+l)%2:
                    if board[k][l] != 'B':
                        start_w += 1
                    if board[k][l] != 'W':
                        start_b += 1
                # 행과 열의 합이 짝수일 때
                else:
                    if board[k][l] != 'B':
                        start_b += 1
                    if board[k][l] != 'W':
                        start_w += 1
        # 최소 변화량을 계산하여 갱신
        if min(start_b, start_w) < answer:
            answer = min(start_b, start_w)
print(answer)

# 4중 for문 말고 다른 방법!!!