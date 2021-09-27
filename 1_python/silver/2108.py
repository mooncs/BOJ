# 통계학
# import sys
# # 수의 개수
# n = int(sys.stdin.readline().rstrip())
# if n == 1:      # 수가 한개 일 때,
#     num = int(sys.stdin.readline().rstrip())
#     print(num)  # 산술평균
#     print(num)  # 중앙값
#     print(num)  # 최빈값
#     print(0)    # 범위
# else:                           # 그 수가 한 개 이상일 때
#     arr, cnt = [], []           # 수를 담을 리스트 arr, 최빈값을 담을 리스트 cnt
#     counting = {}               # 나온 수의 횟수를 카운팅하기 위한 딕셔너리 counting
#     max_cnt = 0                 # 가장 많이 나온 횟수
#     for _ in range(n):          # n개만큼 수 입력받기
#         num = int(sys.stdin.readline().rstrip())
#         arr.append(num)         # 해당 수를 arr에 담고
#         if counting.get(num):   # 이미 나왔던 수라면 +1
#             counting[num] += 1
#         else:                   # 처음 나온 수라면 카운트 시작
#             counting[num] = 1
#     # 산술평균, N개의 수들의 합을 N으로 나눈 값
#     # 소수점 이하 첫째 자리에서 반올림한 값 출력
#     print('{:.0f}'.format(sum(arr)/n))
#     # print(round(sum(arr)/n))

#     # 중앙값, N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
#     arr.sort()       # 우선적으로 오름차순 정렬
#     print(arr[n//2]) # n은 홀수이기 때문에 2로 나눈몫의 위치값 중앙값
    
#     # 최빈값 : N개의 수들 중 가장 많이 나타나는 값
#     # 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력
#     for k, v in counting.items():
#         if v > max_cnt:         # 카운팅한 숫자가 가장 많이 나온 횟수보다 많다면
#             max_cnt = v         # 가장 많이 나온 횟수 갱신
#             cnt.clear()         # 이전까지의 최빈값들은 의미가 없기에 최신화
#             cnt.append(k)       # 현재 값 최빈값 리스트에 추가
#         elif v == max_cnt:      # 가장 많이 나온 횟수와 동일하다면
#             cnt.append(k)       # 최빈값 리스트에 추가
#     cnt.sort()                  # 두번째로 작은 값을 출력하기 위해 정렬
#     if len(cnt)>1:print(cnt[1]) # 최빈값 리스트가 2개 이상이면 2번째 값 출력
#     else:print(cnt[0])          # 최빈값이 하나라면 최빈값 출력
    
#     # 범위 : N개의 수들 중 최댓값과 최솟값의 차이
#     print(max(arr)-min(arr))


'''
most_common()
Counter 클래스는 데이터의 개수가 많은 순으로 정렬된 배열을 리턴하는
most_common이라는 메서드를 제공하고 있다.
이 메서드의 인자로 숫자 n를 넘기면 그 숫자 만큼만 리턴,
가장 개수가 많은 n개의 데이터

→ most_common()은 빈도수가 높은 순으로 리스트 안의 튜플형태로 반환
'''
import sys
from collections import Counter

n = int(sys.stdin.readline())
if n == 1:      # 수가 한개 일 때,
    num = int(sys.stdin.readline().rstrip())
    print(num)  # 산술평균
    print(num)  # 중앙값
    print(num)  # 최빈값
    print(0)    # 범위
else:
    arr = [int(sys.stdin.readline()) for _ in range(n)]
    # 입력받은 수 정렬
    arr.sort()
    # 빈도수가 높은 순으로 리스트 정렬
    cnt = Counter(arr).most_common()
    # 산술평균
    print(round(sum(arr)/n))
    # 중앙값
    print(arr[n//2])
    # 최빈값
    if cnt[0][1] == cnt[1][1]:
        print(cnt[1][0])
    else: print(cnt[0][0])
    # 범위
    print(arr[-1] - arr[0])
