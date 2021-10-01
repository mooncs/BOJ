# 요세푸스 문제 0
import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
num = deque()
ose = []
for i in range(1, n+1):
    num.append(str(i))
while num:
    for j in range(k-1):
        num.append(num.popleft())
    ose.append(num.popleft())
print('<', end='')
print(', '.join(ose), end='')
print('>')