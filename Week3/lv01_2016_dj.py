# PROGRAMMERS Lv1 2016년
# https://school.programmers.co.kr/learn/courses/30/lessons/12901

# 작성자 : 강동준
# 최초 작성일 : 2022-07-15
# 최종 작성일 : 2022-07-17

def solution(a, b):
    month = ["SUN","MON","TUE","WED","THU","FRI","SAT"]
    day = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    start = 5           # new year start FRIDAY
    answer = ''
    total = 0

    for index in range(1, a):       # the sum up to the previous month
        total += day[index]
    total += b                      # This month's day plus
    
    answer = month[(total + start - 1) % 7]         # This year starts on Friday and starts correcting the difference

    return answer

a = 1
b = 7
answer = solution(a, b)
print(answer)