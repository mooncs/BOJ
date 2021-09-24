# 좌표 정렬하기 2
import sys
n = int(sys.stdin.readline().rstrip())
answer = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
answer.sort(key=lambda x: (x[1], x[0]))
for a in answer:
    print(*a)