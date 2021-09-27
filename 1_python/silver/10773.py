# 제로
import sys
k = int(sys.stdin.readline())
st = []
for _ in range(k):
    num = int(sys.stdin.readline())
    if not num:st.pop()
    else:st.append(num)
print(sum(st))