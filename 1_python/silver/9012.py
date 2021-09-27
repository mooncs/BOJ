# 괄호
import sys
for _ in range(int(sys.stdin.readline())):
    vps = sys.stdin.readline().rstrip()
    st = []
    for ps in vps:
        if ps == '(':
            st.append(ps)
        elif ps == ')' and st and st[-1]=='(':
            st.pop()
        else:
            print('NO')
            break
    else:
        if st:print('NO')
        else:print('YES')