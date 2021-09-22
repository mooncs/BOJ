# 직각삼각형
# 피타고라스의 정리 활용
while True:
    triangle = list(map(int, input().split()))
    if triangle[0]==0 and triangle[1]==0 and triangle[2]==0:
        exit()
    triangle.sort()
    if triangle[2]**2 == triangle[0]**2 + triangle[1]**2:
        print("right")
    else:
        print("wrong")