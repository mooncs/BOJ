# 단어 정렬
# 116ms, 셋
import sys
n = int(sys.stdin.readline())
words = set()
for _ in range(n):
    words.add(sys.stdin.readline().rstrip())
words = list(words)
words.sort(key=lambda x: (len(x), x))
print(*words, sep='\n')

# # 3844ms, 리스트
# import sys
# n = int(sys.stdin.readline())
# words = []
# for _ in range(n):
#     word = sys.stdin.readline().rstrip()
#     if word not in words:
#         words.append(word)
# words.sort(key=lambda x: (len(x), x))
# print(*words, sep='\n')