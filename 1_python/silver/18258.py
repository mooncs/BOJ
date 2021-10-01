# 큐 2
import sys
from collections import deque
q = deque()
for _ in range(int(sys.stdin.readline())):
    cmd = sys.stdin.readline().rstrip()
    if cmd[:4] == 'push':
        c, n = cmd.split()
        q.append(int(n))
    elif cmd == 'pop':
        if q:print(q.popleft())
        else:print(-1)
    elif cmd == 'size':
        print(len(q))
    elif cmd == 'empty':
        if q:print(0)
        else:print(1)
    elif cmd == 'front':
        if q:print(q[0])
        else:print(-1)
    elif cmd == 'back':
        if q:print(q[-1])
        else:print(-1)

# # 시간초과
# import sys
# q = []
# for _ in range(int(sys.stdin.readline())):
#     cmd = sys.stdin.readline().rstrip()
#     if cmd[:4] == 'push':
#         c, n = cmd.split()
#         q.append(int(n))
#     elif cmd == 'pop':
#         if q:print(q.pop(0))
#         else:print(-1)
#     elif cmd == 'size':
#         print(len(q))
#     elif cmd == 'empty':
#         if q:print(0)
#         else:print(1)
#     elif cmd == 'front':
#         if q:print(q[0])
#         else:print(-1)
#     elif cmd == 'back':
#         if q:print(q[-1])
#         else:print(-1)