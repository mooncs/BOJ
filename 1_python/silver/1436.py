# 영화감독 숌
# # 체크해보기
# N = int(input())
# if N==1:
#     print(666)
# else:
#     count = 1
#     for i in range(2, N+1):
#         base_title = "{0}666".format(i-1)
#         num_of_extra_six_in_row = 0
#         for k in range(len(base_title)-3):
#             if base_title[-4-k]=='6':
#                 num_of_extra_six_in_row += 1
#             else:
#                 break
#         count += int(10**num_of_extra_six_in_row)
#         if count >= N:
#             break
            
#     if num_of_extra_six_in_row > 0:
#         base = int(10**num_of_extra_six_in_row)
#         count -= base
#         base_title = int(base_title) - int(base_title)%base + (N - count-1)
        
#     print(base_title)

# 1씩 더하는건 너무 비효율적, 808ms
def shom(n):
    title = 666
    while n > 0:
        if '666' in str(title):
            n -= 1
        title += 1
    return title
n = int(input())
print(shom(n) - 1)

# # 실패 → 너무 단순하게 생각
# n = int(input())
# print((n-1)*1000+666)