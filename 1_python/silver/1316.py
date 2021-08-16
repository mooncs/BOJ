# 1316. 그룹 단어 체커
N = int(input())
# 그룹 단어를 체크할 변수
chk = 0
for tc in range(N):
    word = input()
    for i in range(len(word)-1):
        # 단어의 알파벳이 그 다음 알파벳과 같지 않을 때, 더이상 그 알파벳이 안나와야 그룹 단어이다.
        # 만약 동일 알파벳이 i+2부터 시작되는 단어에 들어있다면 그룹단어가 아니므로 break
        if word[i] != word[i+1] and word[i] in word[i+2:]:
            break
    # break없이 성공적으로 for문을 다 돌았다면, 그룹단어이기 때문에 count
    else:
        chk += 1
print(chk)


