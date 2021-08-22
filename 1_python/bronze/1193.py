# 1193. 분수찾기

# # 실패
X = int(input())

m = 0
end_point = 0
for i in range(1, X+1):
    m += i
    end_point += 1
    if X < m:
        m -= i-1
        break
    elif X == m:
        break
# if end_point == 1:
#     print("1/1")
if end_point % 2:
    for i in range(end_point, -1, -1):
        if X == m:
            print("{}/{}".format(i, end_point+1-i))
            break
        m += 1
else:
    for i in range(1, end_point+1):
        if X == m:
            print("{}/{}".format(i, end_point+1-i))
            break
        m += 1


