# 1712. 손익분기점

# fc : 고정비용
# vc : 가변비용
# p : 가격
# 손익분기점 확인 함수
def break_even(fc, vc, p):
    # 가변비용이 물품의 가격보다 크거나 같다면 절대 이익을 낼 수 없다.
    if vc >= p:
        return -1
    else:
        # 물품의 수, i
        i = fc // (p-vc) + 1
        return i

fc, vc, p = map(int, input().split())

print(break_even(fc, vc, p))


