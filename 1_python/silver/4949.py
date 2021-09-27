# 균형잡힌 세상
import sys
flag=True
while flag:
    sentence = sys.stdin.readline().rstrip()
    if len(sentence) == 1 and sentence=='.':
        flag = False
        continue
    else:
        st = []
        for word in sentence[:-1]:
            if word.isalpha() or word == ' ':
                continue
            if word == '(':
                st.append(word)
            elif word == '[':
                st.append(word)
            elif word == ')' and st and st[-1] == '(':
                st.pop()
            elif word == ']' and st and st[-1] == '[':
                st.pop()
            else:
                print('no')
                break
        else:
            if st:print('no')
            else:print('yes')