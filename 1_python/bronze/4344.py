'''
4344. 평균은 넘겠지

[문제]
대학생 새내기들의 90%는 자신이 반에서 평균은 넘는다고 생각한다. 당신은 그들에게 슬픈 진실을 알려줘야 한다.

[입력]
첫째 줄에는 테스트 케이스의 개수 C가 주어진다.
둘째 줄부터 각 테스트 케이스마다 학생의 수 N(1 ≤ N ≤ 1000, N은 정수)이 첫 수로 주어지고, 
이어서 N명의 점수가 주어진다. 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.

[출력]
각 케이스마다 한 줄씩 평균을 넘는 학생들의 비율을 반올림하여 소수점 셋째 자리까지 출력한다.

[예제 입력]
5
5 50 50 70 80 100
7 100 95 90 80 70 60 50
3 70 90 80
3 70 90 81
9 100 99 98 97 96 95 94 93 91

[예제 출력]
40.000%
57.143%
33.333%
66.667%
55.556%
'''
# fail
C = int(input())
for case in range(C):
    students_scores = input()
    students = int(students_scores[0])
    scores = list( map(int, students_scores[2:].split()) )
    total = 0
    avg = 0
    for score in scores:
        total += score
    avg = total / students
    cnt = 0
    for score in scores:
        if score > avg:
            cnt += 1
    
    # print( f'{round(cnt/ students * 100, 3)}%' )
    print( '{:.3f}%'.format(cnt/ students * 100) )

# C = int(input())
# results = []
# for case in range(C):
#     students_scores = input()
#     students = int(students_scores[0])
#     scores = list( map(int, students_scores[2:].split()) )
#     total = 0
#     avg = 0
#     for score in scores:
#         total += score
#     avg = total / students
#     cnt = 0
#     for score in scores:
#         if score > avg:
#             cnt += 1
#     results.append('{:.3f}%'.format(cnt/ students * 100))

# for result in results:
#     print(result)