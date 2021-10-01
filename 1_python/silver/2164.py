# 카드2
import sys
from collections import deque

cards = deque()
for i in range(1, int(sys.stdin.readline())+1):
    cards.append(i)
while len(cards)>1:
    cards.popleft()
    cards.append(cards.popleft())
print(cards[0])

# # 시간 초과
# import sys

# cards = [i for i in range(1, int(sys.stdin.readline())+1)]
# while len(cards)>1:
#     cards.pop(0)
#     cards.append(cards.pop(0))
# print(cards[0])