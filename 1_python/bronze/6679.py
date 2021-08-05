'''
싱기한 네자리 숫자

[문제]
싱기한 네자리 숫자란, [1000,9999]인 10진수 숫자중에서,  다음의 조건을 만족하는 숫자를 말한다.

숫자를 10진수, 12진수, 16진수로 나타낸 다음, 각각의 숫자에 대해, 각 숫자의 자리수를 더했을 때, 세 값이 모두 같아야 한다.
여러분은 싱기한 네자리 숫자를 모두 출력해야 한다.

[입력]
입력은 주어지지 않는다.

[출력]
싱기한 네자리 숫자를 오름차순으로 한줄에 하나씩 출력한다.

[예제 출력 1] 
2992
2993
2994
2995
2996
2997
2998
2999
힌트
싱기한 네자리 숫자의 첫 번째 수는 2992이다.
'''
def convert_sum(number, to):
    total = 0
    while number > 0:
        total += number % to
        number = number // to
    return total

for i in range(1000, 10000):
    deci = convert_sum(i,10)
    zwolf = convert_sum(i, 12)
    hexa = convert_sum(i, 16)
    if deci == zwolf and zwolf == hexa:
        print(i)

