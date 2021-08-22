# 10828. 스택
# import sys

# def s_push(x, pos):
#     st[pos] = int(x)
#     pos += 1
#     return pos

# def s_pop(pos):
#     if pos == 0:
#         print(-1)
#         return pos
#     else:
#         pos -= 1
#         print(st[pos])
#         return pos

# def s_size():
#     print(pos)

# def s_empty():
#     if pos == 0:
#         print(1)
#     else:
#         print(0)

# def s_top():
#     if pos == 0:
#         print(-1)
#     else: 
#         print(st[pos-1])

# N = int(input())    # 명령의 수
# st = [0]*N          # 명령의 수만큼 칸 생성
# pos = 0             # 현재의 위치
# for _ in range(N):
#     # input()으로 받으면 시간 초과되서
#     x = sys.stdin.readline().rstrip()
#     if 'push' in x:
#         p, num = x.split()
#         pos = s_push(num, pos)
#     elif x == 'pop':
#         pos = s_pop(pos)
#     elif x == 'size':
#         s_size()
#     elif x == 'empty':
#         s_empty()
#     elif x == 'top':
#         s_top()


import sys
N = int(input())    # 명령의 수
st = []
for _ in range(N):
    # 명령 입력
    x = sys.stdin.readline().rstrip()
    if 'push' in x:
        p, num = x.split()
        st.append(num)
    elif x == 'pop':
        if not st:
            print(-1)
        else:
            print(st.pop())
    elif x == 'size':
        print(len(st))
    elif x == 'empty':
        if st:
            print(0)
        else:
            print(1)
    elif x == 'top':
        if not st:
            print(-1)
        else:
            print(st[-1])