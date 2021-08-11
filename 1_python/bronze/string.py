# 11654. 아스키 코드
print(ord(input()))


# 11720. 숫자의 합
N = int(input())
numbers = list(map(int, input()))
total = 0
for num in numbers:
    total += num
print(total)


# 10809. 알파벳 찾기
S = list(input())
alpha = list('abcdefghijklmnopqrstuvwxyz')
idx = [-1 for _ in range(len(alpha))]
for i in range(len(S)-1, -1, -1):
    for j in range(len(alpha)):
        if S[i] in alpha[j]:
            idx[j] = i
for x in idx:
    print(x, end=' ')


# 2675. 문자열 반복
T = int(input())
for tc in range(T):
    R, S = input().split()
    answer=''
    for s in S:
        answer += s*int(R)
    print(answer)


# 	1157. 단어 공부
word = input().upper()
alpha = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
cnt = [0 for _ in range(len(alpha))]

max_cnt = 0
for w in word:
    for i in range(len(alpha)):
        if w == alpha[i]:
            cnt[i] += 1
            if cnt[i] > max_cnt:
                max_cnt = cnt[i]
max_alpha = ''
for j in range(len(cnt)):
    if cnt[j] == max_cnt:
        max_alpha += alpha[j]
if len(max_alpha)>1:
    print("?")
else:
    print(max_alpha)


#  1152. 단어의 개수
sentence = input().strip().split()
print(len(sentence))


# 2908. 상수
A, B = input().split()
A, B = int(A[::-1]), int(B[::-1]) 
if A > B:
    print(A)
else:
    print(B)


# 5622. 다이얼
time = [1+i for i in range(10)]
alpha = ['', '', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
word = input()
total = 0
for w in word:
    for i in range(len(alpha)):
        if w in alpha[i]:
            total += time[i]

print(total)