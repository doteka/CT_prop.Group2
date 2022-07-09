# programmers Lv1 직사각형 별찍기
# https://school.programmers.co.kr/learn/courses/30/lessons/12969

# 작성자 : 강동준
# 최초 작성일 : 2022-07-09
# 최종 작성일 : 2022-07-09

a, b = map(int, input().strip().split(' '))     # split

onLineString = ""                               # init
for i in range(a):                              # a single line
    onLineString += "*"
for i in range(b):                              # loop
    print(onLineString)