# 직사각형에서 탈출
x, y, w, h = map(int, input().split())
# 가장 거리가 짧은 것을 출력
print(min(w-x, h-y, x, y))