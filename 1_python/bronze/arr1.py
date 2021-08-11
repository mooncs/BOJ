# 2562. 최대값
numbers = [int(input()) for _ in range(9)]

max_idx, max_num = 0, 0
for idx, num in enumerate(numbers):
    if num > max_num:
        max_num = num
        max_idx = idx+1
print(max_num, max_idx)


# 2577. 숫자의 개수
A = int(input())
B = int(input())
C = int(input())
multipy = str(A*B*C)
times = [0]*10
for i in multipy:
    times[int(i)] += 1

for time in times:
    print(time)


# 3052. 나머지
remainders = []
for _ in range(10):
    number = int(input())
    remainder = number%42
    if remainder not in remainders:
        remainders.append(remainder)
print(len(remainders))


# 1546. 평균
N = int(input())
scores = list(map(int, input().split()))
for i in range(N-1, 0, -1):
    for j in range(i):
        if scores[j] > scores[j+1]:
            scores[j], scores[j+1] = scores[j+1], scores[j]

max_score = scores[-1]
total = 0
for i in range(N):
    scores[i] = scores[i]/max_score*100
    total += scores[i]

print(total/N)


# 8958. OX퀴즈
T = int(input())
for tc in range(T):
    results = input()
    score = [1 if result=='O' else 0 for result in results]
    total = score[0]
    for i in range(1, len(score)):
        if score[i]:
            score[i] += score[i-1]
            total += score[i]
    
    print(total)


# 4344. 평균은 넘겠지
T = int(input())
for tc in range(T):
    scores = list(map(int, input().split()))
    total = 0
    for i in range(1, len(scores)):
        total += scores[i]
    avg = total/scores[0]
    cnt = 0
    for i in range(1, len(scores)):
        if scores[i] > avg:
            cnt += 1
    print('{:.3f}%'.format(cnt/scores[0]*100))
