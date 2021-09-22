# 달팽이는 올라가고 싶다
# 높이가 V미터인 나무 막대
# 낮에 A미터 올라갈 수 있다. 하지만, 밤에 잠을 자는 동안 B미터 미끄러진다.
A, B, V = map(int, input().split())
# 수식, A*N - B*(N-1) >= V를 이용
if (V-B) % (A-B):
    N = (V-B) // (A-B) + 1
else:
    N = (V-B) // (A-B)
print(N)