# 10950. A+B - 3
T = int(input())
for test in range(T):
    a, b = map(int, input().split())
    print(a + b)


# 8393. 합
N = int(input())
total = 0
for n in range(N):
    total += n+1
print(total)


# 15552. 빠른 A+B
# input 대신 sys.stdin.readline을 사용할 수 있다.(빠른 입출력 방식)
import sys
T = int(input())
for test in range(T):
    a, b = sys.stdin.readline().split()
    print(int(a)+int(b))


# 2741. N 찍기
number = int(input())
for num in range(number):
    print(num+1)


# 2742. 기찍 N
number = int(input())
for num in range(number, 0, -1):
    print(num)


# 11021. A+B - 7
T = int(input())
for test in range(T):
    a, b = map(int, input().split())
    print(f'Case #{test+1}: {a+b}')


# 11022. A+B - 8
T = int(input())
for test in range(T):
    a, b = map(int, input().split())
    print(f'Case #{test+1}: {a} + {b} = {a+b}')


# 2438. 별 찍기 - 1
time = int(input())
for t in range(1, time+1):
    print('*'*t)


# 2439. 별 찍기 - 2
time = int(input())
for t in range(1, time+1):
    print(' '*(time-t)+'*'*t)

for t in range(1, time+1):
    print('{0:>{1}}'.format(('*'*t), time))


# 10871. X보다 작은 수
N, X = map(int, input().split())
numbers = [int(number) for number in input().split()]
for number in numbers:
    if number < X:
        print(number, end=' ')