# PROGRAMMERS Lv2 짝지어 제거하기 
# https://school.programmers.co.kr/learn/courses/30/lessons/12973

# 작성자 : 강동준
# 최초 작성일 : 2022-07-27
# 최종 작성일 : 2022-07-27

def solution(s):
    answer = -1
    count = 0
    stack = []
    c = False
    for key in s:
        if len(stack) > 0:
            if stack[len(stack)-1] == key:
                s = stack[0:len(stack)-1] + s[len(stack)+2:]
                print(s)
        else:
            stack.append(key)

s = "baabaa"
print(solution(s))