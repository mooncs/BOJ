# 10952. A+B - 5
while True:
    a, b = map(int, input().split())
    if a==0 and b==0:
        break
    else:print(a+b)

# 10951. A+B - 4
while True:
    try:
        a, b = map(int, input().split())
        print(a+b)
    except:
        break

# 1110. 더하기 사이클
number = int(input())
if number < 10:
    number *= 10
result = number
cnt = 0
while True:
    result = (result%10 * 10) + ((result//10 + result%10) % 10)
    cnt += 1
    if result == number:
        print(cnt)
        break