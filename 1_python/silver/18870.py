# 좌표 압축
# 1868ms
import sys
n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
uni_num = sorted(set(nums))
idx = {uni_num[i]:i for i in range(len(uni_num))}
print(*[idx[num] for num in nums])


'''
시간 초과
list.index는 리스트의 처음부터 하나씩 차례대로 보면서 해당 원소를 찾기 때문에 
리스트의 길이에 비례하는 시간이 걸린다.
'''
# import sys
# n = int(sys.stdin.readline())
# nums = list(map(int, sys.stdin.readline().split()))
# uni_num = sorted(set(nums))
# for num in nums:
#     print(uni_num.index(num), end=' ')
