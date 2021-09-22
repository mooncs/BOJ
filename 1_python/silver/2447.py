# 별 찍기 - 10
# ★★★★
# 분할 정복 알고리즘(Divide and Conquer)
def stars(n):
    matrix=[]
    for i in range(3 * len(n)):
        if i // len(n) == 1:
            matrix.append(n[i % len(n)] + " " * len(n) + n[i % len(n)])
        else:
            matrix.append(n[i % len(n)] * 3)
    return(list(matrix))

star = ["***","* *","***"]
n = int(input())
k = 0
while n != 3:
    n //= 3
    k += 1
    
for i in range(k):
    star = stars(star)
for i in star:
    print(i)


# 분할 정복 알고리즘
# Divide : 문제가 분할이 가능한 경우, 2개 이상의 문제로 나눈다.
# Conquer : 여전히 분할이 가능하면, 또 다시 Divide를 수행한다. 그렇지 않으면 문제를 푼다.
# ombine : Conquer한 문제들을 통합하여 원래 문제의 답을 얻는다.