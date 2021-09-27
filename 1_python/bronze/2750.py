# 수 정렬하기 1, 2, 3
# 메모리 초과
import sys
# arr = [int(input()) for _ in range(int(input()))]
arr = [int(sys.stdin.readline().rstrip()) for _ in range(int(sys.stdin.readline().rstrip()))]
print(*sorted(arr), sep='\n')