# 4673. 셀프 넘버
def selfNumber():
    numbers = [i for i in range(1, 10001)]
    dNum = []
    for number in numbers:
        if number < 10:
            dNum.append(number*2)
        else:
            d = number
            for n in str(number):
                d += int(n)
            if d not in dNum:
                dNum.append(d)

    selfNum = []
    for num in range(1, 10001):
        if num not in dNum:
            selfNum.append(num)
    
    return selfNum

selfNum = selfNumber()
for self in selfNum:
    print(self)


# 2
def dNumber(num):
    # 생성자가 2자리 수 이상일 경우 자기자신 + 각 자리 수이므로 10으로 나눈 나머지를 통해 합을 구할 수 있다.
    d_num = num
    while num:
        d_num += num % 10
        num //= 10
    return d_num
        
d_numbers = []

for i in range(1,10001):
    d_numbers.append(dNumber(i))
    if i not in d_numbers:
        print(i)