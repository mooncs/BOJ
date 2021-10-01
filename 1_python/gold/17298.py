# 오큰수
import sys
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
st = []
while n:
    n -= 1
    num = arr[n]
    # stack이 존재하고 stack에 있는 수가 현재 수보다 작다면
    while st and st[-1] <= num:
        # stack에서 제외
        st.pop()
    # 스택이 있으면 그 수로 없으면 -1로 갱신        
    arr[n] = st[-1] if st else -1
    # 현재 수를 스택에 넣는다.
    st.append(num)
    
print(*arr)


# # 1
# import sys
# n = int(sys.stdin.readline())
# arr = list(map(int, sys.stdin.readline().split()))
# answer = [-1]*n
# st = []
# for i in range(n):
#     while st and arr[st[-1]] < arr[i]:
#         answer[st.pop()] = arr[i]
#     st.append(i)
# print(*answer)


# # 시간초과
# import sys
# n = int(sys.stdin.readline())
# arr = list(map(int, sys.stdin.readline().split()))
# s, e = 0, 1
# while True:
#     if s == n-1:
#         print(-1)
#         break

#     if e == n:
#         print(-1, end=' ')
#         s += 1
#         e = s + 1
#         continue

#     if arr[s] < arr[e]:
#         print(arr[e], end=' ')
#         s += 1
#         e = s + 1

#     else:
#         e += 1 