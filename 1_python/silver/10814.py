# 나이순 정렬
# 340ms
import sys
n = int(sys.stdin.readline())
members = []
for i in range(n):
    age, name = sys.stdin.readline().rstrip().split()
    members.append((i, int(age), name))
members.sort(key=lambda x: (x[1], x[0]))
for member in members:
    print(member[1], member[2])