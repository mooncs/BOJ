# 블랙잭
# 조합
def combination(idx, s_dix):
    global min_diff, result
    if s_dix == 3:
        if 0 <= m-sum(sel) < min_diff:
            min_diff = m-sum(sel)
            result = sum(sel)
        return

    for i in range(idx, n):
        sel[s_dix] = cards[i]
        combination(i+1, s_dix+1)

n, m = map(int, input().split())
cards = list(map(int, input().split()))
sel = [0]*3 # 선택한 카드 넣을 리스트
result = 0
min_diff = 300000
combination(0, 0)
print(result)