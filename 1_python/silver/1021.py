# 회전하는 큐
import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
targets = list(map(int, sys.stdin.readline().split()))
q = deque(range(1, n+1))
cnt = 0
for target in targets:
    while True:
        if q[0] == target:
            q.popleft()
            break
        else:
            if q.index(target) <= len(q)//2:
                q.rotate(-1)
            else:
                q.rotate(1)
            cnt += 1
print(cnt)