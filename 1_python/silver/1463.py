'''
1463. 1로 만들기

[문제]
정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.
1. X가 3으로 나누어 떨어지면, 3으로 나눈다.
2. X가 2로 나누어 떨어지면, 2로 나눈다.
3. 1을 뺀다.
정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오.

[입력]
첫째 줄에 1보다 크거나 같고, 10^6보다 작거나 같은 정수 N이 주어진다.

[출력]
첫째 줄에 연산을 하는 횟수의 최솟값을 출력한다.
'''

N= int(input())
cnt_lst = [0, 0, 1, 1]

for num in range(4, N+1):
    cnt_lst.append(cnt_lst[num-1] + 1)

    if num%2 == 0:
        cnt_lst[num] = min(cnt_lst[num], cnt_lst[int(num/2)] + 1)

    if num%3 == 0:
        cnt_lst[num] = min(cnt_lst[num], cnt_lst[int(num/3)] + 1)

print(cnt_lst[N])



# N= int(input())
# cnt = 0
# pre_list = [N]

# while True:
#     cnt += 1
#     now_list = []

#     for num in pre_list:
#         if num % 3 == 0:
#             now_list.append(num // 3)

#         if num % 2 == 0:
#             now_list.append(num // 2)

#         now_list.append(num - 1)

#         if 1 in now_list:
#             break
#         elif 0 in now_list:
#             break

#     if 1 in now_list:
#         break
#     elif 0 in now_list:
#         break    

#     pre_list = list(set(now_list))

# if 0 in now_list:
#     print(0)
# else:
#     print(cnt)        