# 1874. 스택 수열
import sys

stack = []
# n = int(input())
n = int(sys.stdin.readline().rstrip())
# seq = [int(input()) for _ in range(n)]
seq = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
seq_i = 0
ans = []
for i in range(1, n+1):
    stack.append(i)
    ans.append('+')
    flag = True
    while flag and stack:
        if stack[len(stack)-1] == seq[seq_i]:
            stack.pop()
            ans.append('-')
            seq_i += 1
        else:
            flag = False
if len(ans) == n*2:
    for a in ans:
        print(a)
else:
    print('NO')