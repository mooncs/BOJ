# 하노이 탑 이동 순서
# ★★
# n 이동할 원반의 수, s 시작점, t 경유지, g 도착점
def hanoi(n, s, t, g):
    if n == 1:
        print(s, g)
    else:
        # 가장 긴 원판을 제외한 나머지를 두번째 장대에 쌓고
        hanoi(n-1, s, g, t)
        # 가장 긴 원판을 마지막 장대로 이동
        print(s, g)
        # 두번째 징대의 것들을 마지막 장대로 이동
        hanoi(n-1, t, s, g)

n = int(input())
# 하노이 탑 이동 횟수는 2ⁿ-1번
print(2**n - 1)
hanoi(n, 1, 2, 3)