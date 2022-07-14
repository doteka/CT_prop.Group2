# programmers Lv1 하샤드 수
# https://school.programmers.co.kr/learn/courses/30/lessons/12947

# 작성자 : 강동준
# 최초 작성일 : 2022-07-08
# 최종 작성일 : 2022-07-08

def solution(x):
    answer = True
    Allplus = sum(map(int, str(x))) # mapping number

    if x % Allplus == 0:
        answer = True
    else:
        answer = False

    return answer

x = 13
a = solution(x)
print(a)