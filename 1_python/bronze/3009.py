# 네 번째 점
xs = []
ys = []
# 네 번째 점은, x좌표 중 한 번만 나온 x좌표와
# y좌표 중 한 번만 나온 y좌표의 조합
for _ in range(3):
    x, y = map(int, input().split())
    if x in xs:
        xs.remove(x)
    else:
        xs.append(x)
    if y in ys:
        ys.remove(y)
    else:
        ys.append(y)
print(xs[0], ys[0])
