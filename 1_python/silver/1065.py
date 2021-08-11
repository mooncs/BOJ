# 1065. 한수
# # 각 자리수를 리스트에 담는 함수 생성
# def divider(num):
#     div = []
#     while num:
#         div.append(num%10)
#         num //= 10
#     return div

# def hansu(N):    
#     # 1~99는 다 한수이기 때문에 i를 출력
#     if N < 100:
#         return N

#     # 한수의 개수 카운트
#     cnt = 99
#     for i in range(100, N+1):
#         # 세자리 수부터는 각 자리 숫자를 받아오고
#         div = divider(i)
#         # 먼저 앞 두자리수의 차이를 구한다.
#         interval = div[1]-div[0]
#         # 한수인지를 체크할 대조군 생성
#         control = [div[0]]
#         # 비교할 숫자의 자리 수만큼 대조군에 interval만큼의 차이를 가진 수 추가
#         for i in range(len(div)-1):
#             control.append(control[i]+interval)
#         # 대조군과 숫자의 구성이 같다면 한수이므로 카운트
#         if div == control:
#             cnt += 1
#     return cnt

# print(hansu(int(input())))


# 2
def hansu(num):
    if num < 100:
        return num
    else:
        cnt = num
        for i in range(100, num+1):
            str_num = str(i)
            interval = int(str_num[1]) - int(str_num[0])
            for j in range(1, len(str_num)-1):
                if int(str_num[j+1]) - int(str_num[j]) != interval:
                    cnt -= 1
                    break
    return cnt

print(hansu(int(input())))


# # 3
# # 1~999까지 들어오기 때문에 세자리 수까지만 고려해도 가능
# def hansu(number):
#     cnt = 0
#     for i in range(1, number+1):
#         if i < 100:
#             cnt += 1
#         else:
#             nums = list(map(int, str(i)))
#             if nums[1]-nums[0] == nums[2]-nums[1]:
#                 cnt += 1
#     return cnt
# print(hansu(int(input())))

