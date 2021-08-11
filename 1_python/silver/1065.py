# 1065. 한수
def divider(num):
    div = []
    while num:
        div.append(num%10)
        num //= 10
    return div

N = int(input())
cnt = 0
for i in range(1, N+1):
    if i < 100:
        cnt += 1
    else:
        div = divider(i)
        interval = div[1]-div[0]
        control = [div[0]]
        for i in range(len(div)-1):
            control.append(control[i]+interval)

        if div == control:
            cnt += 1

print(cnt)


