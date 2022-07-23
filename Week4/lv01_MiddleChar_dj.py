# PROGRAMMERS Lv1 가운데 글자 가져오기
# https://school.programmers.co.kr/learn/courses/30/lessons/64061

# 작성자 : 강동준
# 최초 작성일 : 2022-07-22
# 최종 작성일 : 2022-07-22

def solution(s):
    answer = ''
    length = int(len(s) / 2)
    if len(s) % 2 == 1:
        answer = s[length]
    else:
        answer = s[length-1] + s[length]

    return answer

s = "qwer"
print(solution(s))